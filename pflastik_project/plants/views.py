from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, PlantImage
from .forms import PlantForm, PlantImageForm

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

# PlantImage views
def plant_image_list(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    images = plant.images.all()
    return render(request, 'plant_image_list.html', {'plant': plant, 'images': images})

def plant_image_detail(request, plant_id, image_id):
    image = get_object_or_404(PlantImage, pk=image_id)
    return render(request, 'plant_image_detail.html', {'image': image})

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

def plant_image_delete(request, plant_id, image_id):
    image = get_object_or_404(PlantImage, pk=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('plant_image_list', plant_id=plant_id)
    return render(request, 'plant_image_confirm_delete.html', {'image': image})
