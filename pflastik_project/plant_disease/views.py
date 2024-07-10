

from django.shortcuts import render, get_object_or_404
from .models import Disease, DiseaseImage

# Disease views
def disease_list(request):
    diseases = Disease.objects.all()
    return render(request, 'disease_list.html', {'diseases': diseases})

def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, 'disease_detail.html', {'disease': disease})

# DiseaseImage views
def disease_image_list(request, disease_id):
    disease = get_object_or_404(Disease, pk=disease_id)
    images = disease.images.all()
    return render(request, 'disease_image_list.html', {'disease': disease, 'images': images})

def disease_image_detail(request, disease_id, image_id):
    image = get_object_or_404(DiseaseImage, pk=image_id)
    return render(request, 'disease_image_detail.html', {'image': image})
