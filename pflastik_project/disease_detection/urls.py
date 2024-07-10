# urls.py

from django.urls import path
from .views import (
    DiseaseCategoryListView, DiseaseCategoryDetailView, DiseaseCategoryCreateView,
    DiseaseCategoryUpdateView, DiseaseCategoryDeleteView,
    PlantPartListView, PlantPartDetailView, PlantPartCreateView, PlantPartUpdateView,
    PlantPartDeleteView, DiagnosticSessionListView, DiagnosticSessionDetailView,
    DiagnosticSessionCreateView, DiagnosticSessionUpdateView, DiagnosticSessionDeleteView
)

app_name = 'your_app_name'

urlpatterns = [
    # DiseaseCategory URLs
    path('disease_categories/', DiseaseCategoryListView.as_view(), name='disease_category_list'),
    path('disease_category/<int:pk>/', DiseaseCategoryDetailView.as_view(), name='disease_category_detail'),
    path('disease_category/create/', DiseaseCategoryCreateView.as_view(), name='disease_category_create'),
    path('disease_category/<int:pk>/update/', DiseaseCategoryUpdateView.as_view(), name='disease_category_update'),
    path('disease_category/<int:pk>/delete/', DiseaseCategoryDeleteView.as_view(), name='disease_category_delete'),

    # PlantPart URLs
    path('plant_parts/', PlantPartListView.as_view(), name='plant_part_list'),
    path('plant_part/<int:pk>/', PlantPartDetailView.as_view(), name='plant_part_detail'),
    path('plant_part/create/', PlantPartCreateView.as_view(), name='plant_part_create'),
    path('plant_part/<int:pk>/update/', PlantPartUpdateView.as_view(), name='plant_part_update'),
    path('plant_part/<int:pk>/delete/', PlantPartDeleteView.as_view(), name='plant_part_delete'),

    # DiagnosticSession URLs
    path('diagnostic_sessions/', DiagnosticSessionListView.as_view(), name='diagnostic_session_list'),
    path('diagnostic_session/<int:pk>/', DiagnosticSessionDetailView.as_view(), name='diagnostic_session_detail'),
    path('diagnostic_session/create/', DiagnosticSessionCreateView.as_view(), name='diagnostic_session_create'),
    path('diagnostic_session/<int:pk>/update/', DiagnosticSessionUpdateView.as_view(), name='diagnostic_session_update'),
    path('diagnostic_session/<int:pk>/delete/', DiagnosticSessionDeleteView.as_view(), name='diagnostic_session_delete'),
]
