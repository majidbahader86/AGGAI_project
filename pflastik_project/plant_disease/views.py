from django.shortcuts import render, redirect
from .forms import DiseaseCategoryForm, PlantPartForm, DiseaseForm, DiseaseImageForm, PlantForm, PlantImageForm
from .models import DiseaseCategory, PlantPart, Disease, EuropeanDisease,  DiseaseImage, Plant, PlantImage

def add_disease_category(request):
    if request.method == 'POST':
        form = DiseaseCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_library')
    else:
        form = DiseaseCategoryForm()
    return render(request, 'add_disease_category.html', {'form': form})

def add_plant_part(request):
    if request.method == 'POST':
        form = PlantPartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_library')
    else:
        form = PlantPartForm()
    return render(request, 'add_plant_part.html', {'form': form})

def add_disease(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_library')
    else:
        form = DiseaseForm()
    return render(request, 'add_disease.html', {'form': form})

# European Diseases Views
@login_required
def create_european_disease(request):
    if request.method == 'POST':
        form = EuropeanDiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('european_disease_list')
    else:
        form = EuropeanDiseaseForm()
    return render(request, 'create_european_disease.html', {'form': form})

def add_disease_image(request):
    if request.method == 'POST':
        form = DiseaseImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('disease_library')
    else:
        form = DiseaseImageForm()
    return render(request, 'add_disease_image.html', {'form': form})

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_library')
    else:
        form = PlantForm()
    return render(request, 'add_plant.html', {'form': form})

def add_plant_image(request):
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('disease_library')
    else:
        form = PlantImageForm()
    return render(request, 'add_plant_image.html', {'form': form})