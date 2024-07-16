# forms.py
from django import forms
from .models import DiseaseIdentificationRequest

class DiseaseIdentificationRequestForm(forms.ModelForm):
    class Meta:
        model = DiseaseIdentificationRequest
        fields = ['image', 'ai_requested']
        widgets = {
            'ai_requested': forms.CheckboxInput(),
        }