from django.urls import path
from . import views

urlpatterns = [
    path('add-disease-category/', views.add_disease_category, name='add_disease_category'),
    path('add-plant-part/', views.add_plant_part, name='add_plant_part'),
    path('add-disease/', views.add_disease, name='add_disease'),
    path('add-disease-image/', views.add_disease_image, name='add_disease_image'),
    path('add-plant/', views.add_plant, name='add_plant'),
    path('add-plant-image/', views.add_plant_image, name='add_plant_image'),
]
