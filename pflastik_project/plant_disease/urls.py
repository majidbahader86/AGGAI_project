from django.urls import path
from . import views

urlpatterns = [
    # Plant URLs
    path('plants/', views.plant_list, name='plant_list'),
    path('plants/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plants/create/', views.plant_create, name='plant_create'),
    path('plants/<int:pk>/update/', views.plant_update, name='plant_update'),
    path('plants/<int:pk>/delete/', views.plant_delete, name='plant_delete'),

    # Plant Image URLs
    path('plants/<int:plant_id>/images/', views.plant_image_list, name='plant_image_list'),
    path('plants/<int:plant_id>/images/<int:image_id>/', views.plant_image_detail, name='plant_image_detail'),
    path('plants/<int:plant_id>/images/create/', views.plant_image_create, name='plant_image_create'),
    path('plants/<int:plant_id>/images/<int:image_id>/update/', views.plant_image_update, name='plant_image_update'),
    path('plants/<int:plant_id>/images/<int:image_id>/delete/', views.plant_image_delete, name='plant_image_delete'),

    # Disease Category URLs
    path('disease_categories/add/', views.add_disease_category, name='add_disease_category'),

    # Plant Part URLs
    path('plant_parts/add/', views.add_plant_part, name='add_plant_part'),

    # Disease URLs
    path('diseases/add/', views.add_disease, name='add_disease'),

    # European Diseases URLs
    path('european_diseases/create/', views.create_european_disease, name='create_european_disease'),

    # Disease Image URLs
    path('disease_images/add/', views.add_disease_image, name='add_disease_image'),

    # Additional Plant URLs (if needed)
    path('plants/add/', views.add_plant, name='add_plant'),

    # Additional Plant Image URLs (if needed)
    path('plant_images/add/', views.add_plant_image, name='add_plant_image'),
]
