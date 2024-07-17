
# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('disease-categories/', views.DiseaseCategoryListCreateAPIView.as_view(), name='disease-category-list'),
    path('disease-categories/<int:pk>/', views.DiseaseCategoryRetrieveUpdateDestroyAPIView.as_view(), name='disease-category-detail'),
    path('plant-parts/', views.PlantPartListCreateAPIView.as_view(), name='plant-part-list'),
    path('plant-parts/<int:pk>/', views.PlantPartRetrieveUpdateDestroyAPIView.as_view(), name='plant-part-detail'),
    path('diseases/', views.DiseaseListCreateAPIView.as_view(), name='disease-list'),
    path('diseases/<int:pk>/', views.DiseaseRetrieveUpdateDestroyAPIView.as_view(), name='disease-detail'),
    path('disease-images/', views.DiseaseImageListCreateAPIView.as_view(), name='disease-image-list'),
    path('disease-images/<int:pk>/', views.DiseaseImageRetrieveUpdateDestroyAPIView.as_view(), name='disease-image-detail'),
    path('european-diseases/', views.EuropeanDiseaseListCreateAPIView.as_view(), name='european-disease-list'),
    path('european-diseases/<int:pk>/', views.EuropeanDiseaseRetrieveUpdateDestroyAPIView.as_view(), name='european-disease-detail'),
    path('plants/', views.PlantListCreateAPIView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', views.PlantRetrieveUpdateDestroyAPIView.as_view(), name='plant-detail'),
]
