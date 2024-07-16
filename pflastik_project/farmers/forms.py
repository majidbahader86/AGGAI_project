from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import (
    MonitoringData, MonitoringAlert, MonitoringAction, 
    ForumPost, ForumComment, SeasonAlert, EnvironmentalCondition, 
    CareTip, FinancialAid
)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)

# Monitoring Forms
class MonitoringDataForm(forms.ModelForm):
    class Meta:
        model = MonitoringData
        fields = ['temperature', 'humidity', 'soil_moisture']

class MonitoringAlertForm(forms.ModelForm):
    class Meta:
        model = MonitoringAlert
        fields = ['alert_type', 'alert_message']

class MonitoringActionForm(forms.ModelForm):
    class Meta:
        model = MonitoringAction
        fields = ['name']

# Forum Forms
class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['content']

# Seasonal Alerts Form
class SeasonAlertForm(forms.ModelForm):
    class Meta:
        model = SeasonAlert
        fields = ['crop', 'alert_type', 'alert_message']

# Environmental Conditions Form
class EnvironmentalConditionForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalCondition
        fields = ['temperature', 'humidity', 'soil_moisture', 'alert_message']

# Care Tips Form
class CareTipForm(forms.ModelForm):
    class Meta:
        model = CareTip
        fields = ['crop', 'region', 'tip']

# Financial Aid Form
class FinancialAidForm(forms.ModelForm):
    class Meta:
        model = FinancialAid
        fields = ['crop', 'price', 'transaction_date']
