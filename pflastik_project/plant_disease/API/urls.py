# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DiseaseCategoryViewSet, PlantPartViewSet, DiseaseViewSet, 
    DiseaseImageViewSet, EuropeanDiseaseViewSet, PlantViewSet, PlantImageViewSet
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
    path('api/', include(router.urls)),
]
