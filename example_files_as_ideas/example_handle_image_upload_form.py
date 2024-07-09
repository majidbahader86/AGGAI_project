from django import forms
from .models.upload import PlantImage

class PlantImageForm(forms.ModelForm):
    class Meta:
        model = PlantImage
        fields = ['image']
