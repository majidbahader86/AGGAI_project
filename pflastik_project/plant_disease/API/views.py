# views.py
from rest_framework import viewsets
from ..models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant, PlantImage
from .serializers import (
    DiseaseCategorySerializer, PlantPartSerializer, DiseaseSerializer, 
    DiseaseImageSerializer, EuropeanDiseaseSerializer, PlantSerializer, PlantImageSerializer
)

class DiseaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = DiseaseCategory.objects.all()
    serializer_class = DiseaseCategorySerializer

class PlantPartViewSet(viewsets.ModelViewSet):
    queryset = PlantPart.objects.all()
    serializer_class = PlantPartSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseImageViewSet(viewsets.ModelViewSet):
    queryset = DiseaseImage.objects.all()
    serializer_class = DiseaseImageSerializer

class EuropeanDiseaseViewSet(viewsets.ModelViewSet):
    queryset = EuropeanDisease.objects.all()
    serializer_class = EuropeanDiseaseSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantImageViewSet(viewsets.ModelViewSet):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
