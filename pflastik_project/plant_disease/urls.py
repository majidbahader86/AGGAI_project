from django.urls import path
from . import views

urlpatterns = [
    # Disease Category URLs
    path('disease/categories/', views.disease_category_list, name='disease_category_list'),
    path('disease/categories/create/', views.disease_category_create, name='disease_category_create'),
    path('disease/categories/<int:pk>/', views.disease_category_detail, name='disease_category_detail'),
    path('disease/categories/<int:pk>/update/', views.disease_category_update, name='disease_category_update'),
    path('disease/categories/<int:pk>/delete/', views.disease_category_delete, name='disease_category_delete'),

    # Plant Part URLs
    path('plant/parts/', views.plant_part_list, name='plant_part_list'),
    path('plant/parts/create/', views.plant_part_create, name='plant_part_create'),
    path('plant/parts/<int:pk>/', views.plant_part_detail, name='plant_part_detail'),
    path('plant/parts/<int:pk>/update/', views.plant_part_update, name='plant_part_update'),
    path('plant/parts/<int:pk>/delete/', views.plant_part_delete, name='plant_part_delete'),

    # Disease URLs
    path('diseases/', views.disease_list, name='disease_list'),
    path('diseases/create/', views.disease_create, name='disease_create'),
    path('diseases/<int:pk>/', views.disease_detail, name='disease_detail'),
    path('diseases/<int:pk>/update/', views.disease_update, name='disease_update'),
    path('diseases/<int:pk>/delete/', views.disease_delete, name='disease_delete'),

    # Disease Image URLs
    path('disease/images/', views.disease_image_list, name='disease_image_list'),
    path('disease/images/create/', views.disease_image_create, name='disease_image_create'),
    path('disease/images/<int:pk>/', views.disease_image_detail, name='disease_image_detail'),
    path('disease/images/<int:pk>/update/', views.disease_image_update, name='disease_image_update'),
    path('disease/images/<int:pk>/delete/', views.disease_image_delete, name='disease_image_delete'),

    # European Disease URLs
    path('european/diseases/', views.european_disease_list, name='european_disease_list'),
    path('european/diseases/create/', views.european_disease_create, name='european_disease_create'),
    path('european/diseases/<int:pk>/', views.european_disease_detail, name='european_disease_detail'),
    path('european/diseases/<int:pk>/update/', views.european_disease_update, name='european_disease_update'),
    path('european/diseases/<int:pk>/delete/', views.european_disease_delete, name='european_disease_delete'),

    # Plant URLs
    path('plants/', views.plant_list, name='plant_list'),
    path('plants/create/', views.plant_create, name='plant_create'),
    path('plants/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plants/<int:pk>/update/', views.plant_update, name='plant_update'),
    path('plants/<int:pk>/delete/', views.plant_delete, name='plant_delete'),

    # Plant Image URLs
    path('plant/images/', views.plant_image_list, name='plant_image_list'),
    path('plant/images/create/', views.plant_image_create, name='plant_image_create'),
    path('plant/images/<int:pk>/', views.plant_image_detail, name='plant_image_detail'),
    path('plant/images/<int:pk>/update/', views.plant_image_update, name='plant_image_update'),
    path('plant/images/<int:pk>/delete/', views.plant_image_delete, name='plant_image_delete'),
]
