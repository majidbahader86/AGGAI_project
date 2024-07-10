from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class FarmerSignUpForm(UserCreationForm):
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
        return user

class FarmerLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_farmer:
            raise forms.ValidationError(
                "There was an error with your login.",
                code='invalid_login',
            )
