# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('disease-categories/', views.disease_category_list, name='disease_category_list'),
    path('disease-categories/<int:pk>/', views.disease_category_detail, name='disease_category_detail'),
    path('plant-parts/', views.plant_part_list, name='plant_part_list'),
    path('plant-parts/<int:pk>/', views.plant_part_detail, name='plant_part_detail'),
    path('diseases/', views.disease_list, name='disease_list'),
    path('diseases/<int:pk>/', views.disease_detail, name='disease_detail'),
    path('disease-images/', views.disease_image_list, name='disease_image_list'),
    path('disease-images/<int:pk>/', views.disease_image_detail, name='disease_image_detail'),
    path('plants/', views.plant_list, name='plant_list'),
    path('plants/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant-images/', views.plant_image_list, name='plant_image_list'),
    path('plant-images/<int:pk>/', views.plant_image_detail, name='plant_image_detail'),
    
    # Create and Update Views
    path('create/disease-category/', views.create_disease_category, name='create_disease_category'),
    path('create/plant-part/', views.create_plant_part, name='create_plant_part'),
    path('create/disease/', views.create_disease, name='create_disease'),
    path('create/disease-image/', views.create_disease_image, name='create_disease_image'),
    path('create/plant/', views.create_plant, name='create_plant'),
    path('create/plant-image/', views.create_plant_image, name='create_plant_image'),
]
