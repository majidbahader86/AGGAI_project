from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.update_user_profile, name='profile'),
    path('profile/update_profile/', views.update_profile, name='update_profile'),
    path('profile/update_user/', views.update_user, name='update_user'),
]