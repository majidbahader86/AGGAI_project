from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
]