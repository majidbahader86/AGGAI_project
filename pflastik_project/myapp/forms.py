from django import forms
from .models import Image

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
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 5mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")