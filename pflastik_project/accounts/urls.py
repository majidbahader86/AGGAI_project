from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('update_profile/<int:profile_id>/', views.update_profile, name='update_profile'),
    path('update_foo/<int:foo_id>/', views.update_foo, name='update_foo'),
]

