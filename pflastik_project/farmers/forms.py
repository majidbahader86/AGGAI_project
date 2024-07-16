from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import MonitoringData, MonitoringAction, MonitoringAlert, ForumPost, ForumComment, \
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
from django import forms


class MonitoringDataForm(forms.ModelForm):
    class Meta:
        model = MonitoringData
        exclude = ['timestamp'] 

class MonitoringAlertForm(forms.ModelForm):
    class Meta:
        model = MonitoringAlert
        fields = ['alert_type', 'alert_message']


class MonitoringActionForm(forms.ModelForm):
    class Meta:
        model = MonitoringAction
        fields = ['name']

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['user', 'title', 'content']

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['post', 'user', 'content']

class SeasonAlertForm(forms.ModelForm):
    class Meta:
        model = SeasonAlert
        fields = ['crop', 'alert_type', 'alert_message']
class EnvironmentalConditionForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalCondition
        exclude = ['timestamp']  # Exclude the auto-generated timestamp field


class CareTipForm(forms.ModelForm):
    class Meta:
        model = CareTip
        fields = ['crop', 'region', 'tip']

class FinancialAidForm(forms.ModelForm):
    class Meta:
        model = FinancialAid
        fields = ['crop', 'price', 'transaction_date']

# New Forms for Farmers

class FarmerSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_farmer = True  # Assuming you have a boolean field is_farmer in your User model
        if commit:
            user.save()
            # Create a corresponding Profile instance
            Profile.objects.create(user=user)
        return user

class FarmerLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not hasattr(user, 'profile') or not user.profile.is_farmer:
            raise forms.ValidationError(
                "There was an error with your login.",
                code='invalid_login',
            )