from django.urls import path
from . import views

urlpatterns = [
    path('disease_identification_request/create/', views.create_disease_identification_request, name='create_disease_identification_request'),
    path('disease_identification_requests/', views.list_disease_identification_requests, name='list_disease_identification_requests'),
]