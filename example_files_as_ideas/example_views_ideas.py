from django.shortcuts import render
from .models.common import PlantDisease
from .models.scientist import ScientistInfo
from .models.farmer import FarmerInfo

def scientist_view(request):
    diseases = PlantDisease.objects.all()
    scientist_info = ScientistInfo.objects.select_related('disease').all()
    return render(request, 'scientist/disease_list.html', {'diseases': diseases, 'info': scientist_info})

def farmer_view(request):
    diseases = PlantDisease.objects.all()
    farmer_info = FarmerInfo.objects.select_related('disease').all()
    return render(request, 'farmer/disease_list.html', {'diseases': diseases, 'info': farmer_info})
