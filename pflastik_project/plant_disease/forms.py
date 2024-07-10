from django import forms
from .models import DiseaseIdentificationRequest, ForumPost, ForumComment, SeasonAlert
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class DiseaseIdentificationRequestForm(forms.ModelForm):
    class Meta:
        model = DiseaseIdentificationRequest
        fields = ['image', 'ai_requested']

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['content']

class SeasonAlertForm(forms.ModelForm):
    class Meta:
        model = SeasonAlert
        fields = ['crop', 'alert_type', 'alert_message']

class FarmerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FarmerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
