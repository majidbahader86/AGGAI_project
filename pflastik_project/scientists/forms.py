from django import forms
from .models import Publication, AIToolUsage, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'author', 'abstract', 'content', 'published_date', 'category', 'file', 'external_link']

class AIToolUsageForm(forms.ModelForm):
    class Meta:
        model = AIToolUsage
        fields = ['tool', 'user', 'input_data', 'result']

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
