# forms.py

from django import forms
from .models import DiseaseCategory, PlantPart, DiagnosticSession

class DiseaseCategoryForm(forms.ModelForm):
    class Meta:
        model = DiseaseCategory
        fields = ['name', 'description']

class PlantPartForm(forms.ModelForm):
    class Meta:
        model = PlantPart
        fields = ['name', 'description']

class DiagnosticSessionForm(forms.ModelForm):
    class Meta:
        model = DiagnosticSession
        fields = ['name', 'description', 'start_date', 'end_date']
