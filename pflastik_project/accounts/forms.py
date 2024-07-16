from django import forms
from django.contrib.auth.models import User
from .models import Profile, Foo

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_farmer', 'is_scientist']

class FooForm(forms.ModelForm):
    class Meta:
        model = Foo
        fields = ['user']