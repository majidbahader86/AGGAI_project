from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('plant/create/', views.plant_create, name='plant_create'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant/<int:pk>/edit/', views.plant_update, name='plant_update'),
    path('plant/<int:pk>/delete/', views.plant_delete, name='plant_delete'),
    path('plant/<int:plant_id>/images/', views.plant_image_list, name='plant_image_list'),
    path('plant/<int:plant_id>/image/create/', views.plant_image_create, name='plant_image_create'),
    path('plant/<int:plant_id>/image/<int:image_id>/', views.plant_image_detail, name='plant_image_detail'),
    path('plant/<int:plant_id>/image/<int:image_id>/edit/', views.plant_image_update, name='plant_image_update'),
    path('plant/<int:plant_id>/image/<int:image_id>/delete/', views.plant_image_delete, name='plant_image_delete'),
]
