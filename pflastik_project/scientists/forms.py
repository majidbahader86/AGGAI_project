from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'author', 'abstract', 'content', 'published_date', 'category', 'file', 'external_link']

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['user', 'title', 'content']

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['post', 'user', 'content']

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ['name', 'field_of_expertise', 'bio', 'contact_info', 'photo']

class DiagnosticSessionForm(forms.ModelForm):
    class Meta:
        model = DiagnosticSession
        fields = ['user', 'plant', 'symptoms', 'diagnosis']

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'content', 'category']

class ScientistSignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

class ScientistSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']