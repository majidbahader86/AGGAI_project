from django.urls import path
from . import views

urlpatterns = [
    # Disease Category URLs
    path('disease_categories/', views.DiseaseCategoryListView.as_view(), name='disease_category_list'),
    path('disease_categories/create/', views.DiseaseCategoryCreateView.as_view(), name='disease_category_create'),
    path('disease_categories/<int:pk>/', views.DiseaseCategoryUpdateView.as_view(), name='disease_category_update'),
    path('disease_categories/<int:pk>/delete/', views.DiseaseCategoryDeleteView.as_view(), name='disease_category_delete'),

    # Plant Part URLs
    path('plant_parts/', views.PlantPartListView.as_view(), name='plant_part_list'),
    path('plant_parts/create/', views.PlantPartCreateView.as_view(), name='plant_part_create'),
    path('plant_parts/<int:pk>/', views.PlantPartUpdateView.as_view(), name='plant_part_update'),
    path('plant_parts/<int:pk>/delete/', views.PlantPartDeleteView.as_view(), name='plant_part_delete'),

    # Disease URLs
    path('diseases/', views.DiseaseListView.as_view(), name='disease_list'),
    path('diseases/create/', views.DiseaseCreateView.as_view(), name='disease_create'),
    path('diseases/<int:pk>/', views.DiseaseUpdateView.as_view(), name='disease_update'),
    path('diseases/<int:pk>/delete/', views.DiseaseDeleteView.as_view(), name='disease_delete'),

    # Disease Image URLs
    path('disease_images/', views.DiseaseImageListView.as_view(), name='disease_image_list'),
    path('disease_images/create/', views.DiseaseImageCreateView.as_view(), name='disease_image_create'),
    path('disease_images/<int:pk>/', views.DiseaseImageUpdateView.as_view(), name='disease_image_update'),
    path('disease_images/<int:pk>/delete/', views.DiseaseImageDeleteView.as_view(), name='disease_image_delete'),

    # European Disease URLs
    path('european_diseases/', views.EuropeanDiseaseListView.as_view(), name='european_disease_list'),
    path('european_diseases/create/', views.EuropeanDiseaseCreateView.as_view(), name='european_disease_create'),
    path('european_diseases/<int:pk>/', views.EuropeanDiseaseUpdateView.as_view(), name='european_disease_update'),
    path('european_diseases/<int:pk>/delete/', views.EuropeanDiseaseDeleteView.as_view(), name='european_disease_delete'),

    # Plant URLs
    path('plants/', views.PlantListView.as_view(), name='plant_list'),
    path('plants/create/', views.PlantCreateView.as_view(), name='plant_create'),
    path('plants/<int:pk>/', views.PlantUpdateView.as_view(), name='plant_update'),
    path('plants/<int:pk>/delete/', views.PlantDeleteView.as_view(), name='plant_delete'),

    # Plant Image URLs
    path('plant_images/', views.PlantImageListView.as_view(), name='plant_image_list'),
    path('plant_images/create/', views.PlantImageCreateView.as_view(), name='plant_image_create'),
    path('plant_images/<int:pk>/', views.PlantImageUpdateView.as_view(), name='plant_image_update'),
    path('plant_images/<int:pk>/delete/', views.PlantImageDeleteView.as_view(), name='plant_image_delete'),
]
