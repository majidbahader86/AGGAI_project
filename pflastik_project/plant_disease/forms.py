
from django import forms
from .models import DiseaseCategory, PlantPart, Disease, EuropeanDisease, DiseaseImage, Plant, PlantImage

class DiseaseCategoryForm(forms.ModelForm):
    class Meta:
        model = DiseaseCategory
        fields = ['name', 'description']

class PlantPartForm(forms.ModelForm):
    class Meta:
        model = PlantPart
        fields = ['name']

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']
        widgets = {
            'affected_parts': forms.CheckboxSelectMultiple,
        }
        
# Form for European Disease
class EuropeanDiseaseForm(forms.ModelForm):
    class Meta:
        model = EuropeanDisease
        fields = ['name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']
        widgets = {
            'affected_parts': forms.CheckboxSelectMultiple,
        }

class DiseaseImageForm(forms.ModelForm):
    class Meta:
        model = DiseaseImage
        fields = ['disease', 'image', 'description']

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'scientific_name', 'description', 'habitat']

class PlantImageForm(forms.ModelForm):
    class Meta:
        model = PlantImage
        fields = ['plant', 'image', 'description', 'is_healthy']
        

