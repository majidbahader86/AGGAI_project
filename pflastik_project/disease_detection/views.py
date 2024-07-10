# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DiseaseCategory, PlantPart, DiagnosticSession

# DiseaseCategory views
def disease_category_list(request):
    disease_categories = DiseaseCategory.objects.all()
    return render(request, 'disease_category_list.html', {'disease_categories': disease_categories})

def disease_category_detail(request, pk):
    disease_category = get_object_or_404(DiseaseCategory, pk=pk)
    return render(request, 'disease_category_detail.html', {'disease_category': disease_category})

# PlantPart views
def plant_part_list(request):
    plant_parts = PlantPart.objects.all()
    return render(request, 'plant_part_list.html', {'plant_parts': plant_parts})

def plant_part_detail(request, pk):
    plant_part = get_object_or_404(PlantPart, pk=pk)
    return render(request, 'plant_part_detail.html', {'plant_part': plant_part})

# DiagnosticSession views
def diagnostic_session_list(request):
    diagnostic_sessions = DiagnosticSession.objects.all()
    return render(request, 'diagnostic_session_list.html', {'diagnostic_sessions': diagnostic_sessions})

def diagnostic_session_detail(request, pk):
    diagnostic_session = get_object_or_404(DiagnosticSession, pk=pk)
    return render(request, 'diagnostic_session_detail.html', {'diagnostic_session': diagnostic_session})
