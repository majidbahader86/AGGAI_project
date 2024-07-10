# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import DiseaseCategory, PlantPart, DiagnosticSession
from .forms import DiseaseCategoryForm, PlantPartForm, DiagnosticSessionForm

# DiseaseCategory views
class DiseaseCategoryListView(ListView):
    model = DiseaseCategory
    template_name = 'disease_category_list.html'
    context_object_name = 'disease_categories'

class DiseaseCategoryDetailView(DetailView):
    model = DiseaseCategory
    template_name = 'disease_category_detail.html'
    context_object_name = 'disease_category'

@login_required
class DiseaseCategoryCreateView(CreateView):
    model = DiseaseCategory
    template_name = 'disease_category_form.html'
    form_class = DiseaseCategoryForm
    success_url = reverse_lazy('disease_category_list')

@login_required
class DiseaseCategoryUpdateView(UpdateView):
    model = DiseaseCategory
    template_name = 'disease_category_form.html'
    form_class = DiseaseCategoryForm
    success_url = reverse_lazy('disease_category_list')

@login_required
class DiseaseCategoryDeleteView(DeleteView):
    model = DiseaseCategory
    template_name = 'disease_category_confirm_delete.html'
    success_url = reverse_lazy('disease_category_list')

# PlantPart views
class PlantPartListView(ListView):
    model = PlantPart
    template_name = 'plant_part_list.html'
    context_object_name = 'plant_parts'

class PlantPartDetailView(DetailView):
    model = PlantPart
    template_name = 'plant_part_detail.html'
    context_object_name = 'plant_part'

@login_required
class PlantPartCreateView(CreateView):
    model = PlantPart
    template_name = 'plant_part_form.html'
    form_class = PlantPartForm
    success_url = reverse_lazy('plant_part_list')

@login_required
class PlantPartUpdateView(UpdateView):
    model = PlantPart
    template_name = 'plant_part_form.html'
    form_class = PlantPartForm
    success_url = reverse_lazy('plant_part_list')

@login_required
class PlantPartDeleteView(DeleteView):
    model = PlantPart
    template_name = 'plant_part_confirm_delete.html'
    success_url = reverse_lazy('plant_part_list')

# DiagnosticSession views
class DiagnosticSessionListView(ListView):
    model = DiagnosticSession
    template_name = 'diagnostic_session_list.html'
    context_object_name = 'diagnostic_sessions'

class DiagnosticSessionDetailView(DetailView):
    model = DiagnosticSession
    template_name = 'diagnostic_session_detail.html'
    context_object_name = 'diagnostic_session'

@login_required
class DiagnosticSessionCreateView(CreateView):
    model = DiagnosticSession
    template_name = 'diagnostic_session_form.html'
    form_class = DiagnosticSessionForm
    success_url = reverse_lazy('diagnostic_session_list')

@login_required
class DiagnosticSessionUpdateView(UpdateView):
    model = DiagnosticSession
    template_name = 'diagnostic_session_form.html'
    form_class = DiagnosticSessionForm
    success_url = reverse_lazy('diagnostic_session_list')

@login_required
class DiagnosticSessionDeleteView(DeleteView):
    model = DiagnosticSession
    template_name = 'diagnostic_session_confirm_delete.html'
    success_url = reverse_lazy('diagnostic_session_list')
