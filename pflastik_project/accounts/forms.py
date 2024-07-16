from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_farmer = forms.BooleanField(required=False)
    is_scientist = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                is_farmer=self.cleaned_data['is_farmer'],
                is_scientist=self.cleaned_data['is_scientist']
            )
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_farmer', 'is_scientist']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    is_farmer = forms.BooleanField(required=False)
    is_scientist = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ['is_farmer', 'is_scientist']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user.username = self.cleaned_data['username']
        profile.user.email = self.cleaned_data['email']
        if commit:
            profile.user.save()
            profile.save()
        return profile