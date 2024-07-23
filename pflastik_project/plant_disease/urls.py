from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DiseaseCategoryViewSet, PlantPartViewSet, DiseaseViewSet, DiseaseImageViewSet, 
    EuropeanDiseaseViewSet, PlantViewSet, PlantImageViewSet, disease_category_create
)

router = DefaultRouter()
router.register(r'disease-categories', DiseaseCategoryViewSet)
router.register(r'plant-parts', PlantPartViewSet)
router.register(r'diseases', DiseaseViewSet)
router.register(r'disease-images', DiseaseImageViewSet)
router.register(r'european-diseases', EuropeanDiseaseViewSet)
router.register(r'plants', PlantViewSet)
router.register(r'plant-images', PlantImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-disease-category/', disease_category_create, name='create-disease-category'),
]
