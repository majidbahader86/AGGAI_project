# views.py

from django.shortcuts import render, get_object_or_404
from .models import Plant, PlantImage

# Plant views
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant_detail.html', {'plant': plant})

# PlantImage views
def plant_image_list(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    images = plant.images.all()
    return render(request, 'plant_image_list.html', {'plant': plant, 'images': images})

def plant_image_detail(request, plant_id, image_id):
    image = get_object_or_404(PlantImage, pk=image_id)
    return render(request, 'plant_image_detail.html', {'image': image})
