from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial, DiseaseReport, SciencePaper, PlantsDataset,  Image, AgentResponse

class AgentRequestForm(forms.ModelForm):
    class Meta:
        model = AgentResponse
        fields = ['block_index', 'search_term', 'api_key']
        widgets = {
            'api_key': forms.PasswordInput(), 
        }

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 100 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 100mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")

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

class DiseaseReportForm(forms.ModelForm):
    class Meta:
        model = DiseaseReport
        fields = '__all__'
        widgets = {
            'environmental_conditions': forms.Textarea(attrs={'placeholder': 'Environmental Conditions (JSON format)'})
        }

class SciencePaperForm(forms.ModelForm):
    class Meta:
        model = SciencePaper
        fields = '__all__'
        widgets = {
            'authors': forms.TextInput(attrs={'placeholder': 'Author Names (comma-separated)'}),
            'keywords': forms.Textarea(attrs={'placeholder': 'Keywords (comma-separated)'})
        }

class DatasetForm(forms.ModelForm):
    class Meta:
        model = PlantsDataset
        fields = '__all__'
        widgets = {
            'data_fields': forms.Textarea(attrs={'placeholder': 'Data Fields (comma-separated)'})
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Enter your plant-related search query', max_length=255)
