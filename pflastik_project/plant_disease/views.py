from django.shortcuts import render, get_object_or_404, redirect
from .models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant, PlantImage
from .forms import DiseaseCategoryForm, PlantPartForm, DiseaseForm, DiseaseImageForm, EuropeanDiseaseForm, PlantForm, PlantImageForm

# Disease Category views
def disease_category_list(request):
    categories = DiseaseCategory.objects.all()
    return render(request, 'disease_category_list.html', {'categories': categories})

def disease_category_detail(request, pk):
    category = get_object_or_404(DiseaseCategory, pk=pk)
    return render(request, 'disease_category_detail.html', {'category': category})

def disease_category_create(request):
    if request.method == 'POST':
        form = DiseaseCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_category_list')
    else:
        form = DiseaseCategoryForm()
    return render(request, 'disease_category_form.html', {'form': form})

def disease_category_update(request, pk):
    category = get_object_or_404(DiseaseCategory, pk=pk)
    if request.method == 'POST':
        form = DiseaseCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('disease_category_detail', pk=pk)
    else:
        form = DiseaseCategoryForm(instance=category)
    return render(request, 'disease_category_form.html', {'form': form})

def disease_category_delete(request, pk):
    category = get_object_or_404(DiseaseCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('disease_category_list')
    return render(request, 'disease_category_confirm_delete.html', {'category': category})


# Plant Part views
def plant_part_list(request):
    parts = PlantPart.objects.all()
    return render(request, 'plant_part_list.html', {'parts': parts})

def plant_part_detail(request, pk):
    part = get_object_or_404(PlantPart, pk=pk)
    return render(request, 'plant_part_detail.html', {'part': part})

def plant_part_create(request):
    if request.method == 'POST':
        form = PlantPartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_part_list')
    else:
        form = PlantPartForm()
    return render(request, 'plant_part_form.html', {'form': form})

def plant_part_update(request, pk):
    part = get_object_or_404(PlantPart, pk=pk)
    if request.method == 'POST':
        form = PlantPartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('plant_part_detail', pk=pk)
    else:
        form = PlantPartForm(instance=part)
    return render(request, 'plant_part_form.html', {'form': form})

def plant_part_delete(request, pk):
    part = get_object_or_404(PlantPart, pk=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('plant_part_list')
    return render(request, 'plant_part_confirm_delete.html', {'part': part})


# Disease views
def disease_list(request):
    diseases = Disease.objects.all()
    return render(request, 'disease_list.html', {'diseases': diseases})

def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, 'disease_detail.html', {'disease': disease})

def disease_create(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_list')
    else:
        form = DiseaseForm()
    return render(request, 'disease_form.html', {'form': form})

def disease_update(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('disease_detail', pk=pk)
    else:
        form = DiseaseForm(instance=disease)
    return render(request, 'disease_form.html', {'form': form})

def disease_delete(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    if request.method == 'POST':
        disease.delete()
        return redirect('disease_list')
    return render(request, 'disease_confirm_delete.html', {'disease': disease})


# Disease Image views
def disease_image_list(request):
    images = DiseaseImage.objects.all()
    return render(request, 'disease_image_list.html', {'images': images})

def disease_image_detail(request, pk):
    image = get_object_or_404(DiseaseImage, pk=pk)
    return render(request, 'disease_image_detail.html', {'image': image})

def disease_image_create(request):
    if request.method == 'POST':
        form = DiseaseImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('disease_image_list')
    else:
        form = DiseaseImageForm()
    return render(request, 'disease_image_form.html', {'form': form})

def disease_image_update(request, pk):
    image = get_object_or_404(DiseaseImage, pk=pk)
    if request.method == 'POST':
        form = DiseaseImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('disease_image_detail', pk=pk)
    else:
        form = DiseaseImageForm(instance=image)
    return render(request, 'disease_image_form.html', {'form': form})

def disease_image_delete(request, pk):
    image = get_object_or_404(DiseaseImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('disease_image_list')
    return render(request, 'disease_image_confirm_delete.html', {'image': image})


# European Disease views
def european_disease_list(request):
    diseases = EuropeanDisease.objects.all()
    return render(request, 'european_disease_list.html', {'diseases': diseases})

def european_disease_detail(request, pk):
    disease = get_object_or_404(EuropeanDisease, pk=pk)
    return render(request, 'european_disease_detail.html', {'disease': disease})

def european_disease_create(request):
    if request.method == 'POST':
        form = EuropeanDiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('european_disease_list')
    else:
        form = EuropeanDiseaseForm()
    return render(request, 'european_disease_form.html', {'form': form})

def european_disease_update(request, pk):
    disease = get_object_or_404(EuropeanDisease, pk=pk)
    if request.method == 'POST':
        form = EuropeanDiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('european_disease_detail', pk=pk)
    else:
        form = EuropeanDiseaseForm(instance=disease)
    return render(request, 'european_disease_form.html', {'form': form})

def european_disease_delete(request, pk):
    disease = get_object_or_404(EuropeanDisease, pk=pk)
    if request.method == 'POST':
        disease.delete()
        return redirect('european_disease_list')
    return render(request, 'european_disease_confirm_delete.html', {'disease': disease})


# Plant views
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant_detail.html', {'plant': plant})

def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plant_form.html', {'form': form})

def plant_update(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', pk=pk)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plant_form.html', {'form': form})

def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plant_confirm_delete.html', {'plant': plant})


# Plant Image views
def plant_image_list(request):
    images = PlantImage.objects.all()
    return render(request, 'plant_image_list.html', {'images': images})

def plant_image_detail(request, pk):
    image = get_object_or_404(PlantImage, pk=pk)
    return render(request, 'plant_image_detail.html', {'image': image})

def plant_image_create(request):
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_image_list')
    else:
        form = PlantImageForm()
    return render(request, 'plant_image_form.html', {'form': form})

def plant_image_update(request, pk):
    image = get_object_or_404(PlantImage, pk=pk)
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('plant_image_detail', pk=pk)
    else:
        form = PlantImageForm(instance=image)
    return render(request, 'plant_image_form.html', {'form': form})

def plant_image_delete(request, pk):
    image = get_object_or_404(PlantImage, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('plant_image_list')
    return render(request, 'plant_image_confirm_delete.html', {'image': image})
