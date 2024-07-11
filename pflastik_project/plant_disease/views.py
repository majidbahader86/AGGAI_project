# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import DiseaseCategoryForm, PlantPartForm, DiseaseForm, DiseaseImageForm, PlantForm, PlantImageForm
from .models import DiseaseCategory, PlantPart, Disease, DiseaseImage, Plant, PlantImage

# List and Detail Views for DiseaseCategory
def disease_category_list(request):
    categories = DiseaseCategory.objects.all()
    return render(request, 'disease_category_list.html', {'categories': categories})

def disease_category_detail(request, pk):
    category = get_object_or_404(DiseaseCategory, pk=pk)
    return render(request, 'disease_category_detail.html', {'category': category})

# List and Detail Views for PlantPart
def plant_part_list(request):
    parts = PlantPart.objects.all()
    return render(request, 'plant_part_list.html', {'parts': parts})

def plant_part_detail(request, pk):
    part = get_object_or_404(PlantPart, pk=pk)
    return render(request, 'plant_part_detail.html', {'part': part})

# List and Detail Views for Disease
def disease_list(request):
    diseases = Disease.objects.all()
    return render(request, 'disease_list.html', {'diseases': diseases})

def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, 'disease_detail.html', {'disease': disease})

# List and Detail Views for DiseaseImage
def disease_image_list(request):
    images = DiseaseImage.objects.all()
    return render(request, 'disease_image_list.html', {'images': images})

def disease_image_detail(request, pk):
    image = get_object_or_404(DiseaseImage, pk=pk)
    return render(request, 'disease_image_detail.html', {'image': image})

# List and Detail Views for Plant
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant_detail.html', {'plant': plant})

# List and Detail Views for PlantImage
def plant_image_list(request):
    images = PlantImage.objects.all()
    return render(request, 'plant_image_list.html', {'images': images})

def plant_image_detail(request, pk):
    image = get_object_or_404(PlantImage, pk=pk)
    return render(request, 'plant_image_detail.html', {'image': image})

# Create Views for Forms
def create_disease_category(request):
    if request.method == "POST":
        form = DiseaseCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_category_list')
    else:
        form = DiseaseCategoryForm()
    return render(request, 'form_template.html', {'form': form})

def create_plant_part(request):
    if request.method == "POST":
        form = PlantPartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_part_list')
    else:
        form = PlantPartForm()
    return render(request, 'form_template.html', {'form': form})

def create_disease(request):
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_list')
    else:
        form = DiseaseForm()
    return render(request, 'form_template.html', {'form': form})

def create_disease_image(request):
    if request.method == "POST":
        form = DiseaseImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('disease_image_list')
    else:
        form = DiseaseImageForm()
    return render(request, 'form_template.html', {'form': form})

def create_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'form_template.html', {'form': form})

def create_plant_image(request):
    if request.method == "POST":
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_image_list')
    else:
        form = PlantImageForm()
    return render(request, 'form_template.html', {'form': form})
