from django.urls import path
from . import views

urlpatterns = [
    path('scientist/', views.scientist_view, name='scientist_view'),
    path('farmer/', views.farmer_view, name='farmer_view'),
    path('upload/', views.upload_image, name='upload_image'),
]
