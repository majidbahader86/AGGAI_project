from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PlantImageForm
from .models.upload import PlantImage
from .ai_processing import analyze_plant_image

def upload_image(request):
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save()
            # Analyze the image using the AI model
            analysis_result = analyze_plant_image(plant_image.image.path)
            return render(request, 'results.html', {'result': analysis_result})
    else:
        form = PlantImageForm()
    return render(request, 'upload.html', {'form': form})
