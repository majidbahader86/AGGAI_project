from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    DiseaseCategoryForm, PlantPartForm, DiseaseForm, EuropeanDiseaseForm, 
    DiseaseImageForm, PlantForm, PlantImageForm
)
from .models import DiseaseCategory, PlantPart, Disease, EuropeanDisease, DiseaseImage, Plant, PlantImage

# Helper function to handle form submission
def handle_form_submission(request, form_class, template_name, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES if request.FILES else None)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

# Plant views
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant_detail.html', {'plant': plant})

@login_required
def plant_create(request):
    return handle_form_submission(request, PlantForm, 'plant_form.html', 'plant_list')

@login_required
def plant_update(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return handle_form_submission(request, PlantForm, 'plant_form.html', 'plant_detail', {'pk': pk}, instance=plant)

@login_required
def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plant_confirm_delete.html', {'plant': plant})

# PlantImage views
def plant_image_list(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    images = plant.images.all()
    return render(request, 'plant_image_list.html', {'plant': plant, 'images': images})

def plant_image_detail(request, plant_id, image_id):
    image = get_object_or_404(PlantImage, pk=image_id)
    return render(request, 'plant_image_detail.html', {'image': image})

@login_required
def plant_image_create(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save(commit=False)
            plant_image.plant = plant
            plant_image.save()
            return redirect('plant_image_list', plant_id=plant.id)
    else:
        form = PlantImageForm()
    return render(request, 'plant_image_form.html', {'form': form})

@login_required
def plant_image_update(request, plant_id, image_id):
    image = get_object_or_404(PlantImage, pk=image_id)
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('plant_image_detail', plant_id=plant_id, image_id=image_id)
    else:
        form = PlantImageForm(instance=image)
    return render(request, 'plant_image_form.html', {'form': form})

@login_required
def plant_image_delete(request, plant_id, image_id):
    image = get_object_or_404(PlantImage, pk=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('plant_image_list', plant_id=plant_id)
    return render(request, 'plant_image_confirm_delete.html', {'image': image})

# Disease Category Views
def add_disease_category(request):
    return handle_form_submission(request, DiseaseCategoryForm, 'add_disease_category.html', 'disease_library')

# Plant Part Views
def add_plant_part(request):
    return handle_form_submission(request, PlantPartForm, 'add_plant_part.html', 'disease_library')

# Disease Views
def add_disease(request):
    return handle_form_submission(request, DiseaseForm, 'add_disease.html', 'disease_library')

# European Diseases Views
@login_required
def create_european_disease(request):
    return handle_form_submission(request, EuropeanDiseaseForm, 'create_european_disease.html', 'european_disease_list')

# Disease Image Views
def add_disease_image(request):
    return handle_form_submission(request, DiseaseImageForm, 'add_disease_image.html', 'disease_library')

# Plant Views
def add_plant(request):
    return handle_form_submission(request, PlantForm, 'add_plant.html', 'disease_library')

# Plant Image Views
def add_plant_image(request):
    return handle_form_submission(request, PlantImageForm, 'add_plant_image.html', 'disease_library')
