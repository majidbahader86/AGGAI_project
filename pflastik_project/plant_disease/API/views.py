# api/views.py
from rest_framework import generics
from ..models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant
from .serializers import (
    DiseaseCategorySerializer, PlantPartSerializer, DiseaseSerializer,
    DiseaseImageSerializer, EuropeanDiseaseSerializer, PlantSerializer,
)

class DiseaseCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = DiseaseCategory.objects.all()
    serializer_class = DiseaseCategorySerializer

class DiseaseCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiseaseCategory.objects.all()
    serializer_class = DiseaseCategorySerializer

class PlantPartListCreateAPIView(generics.ListCreateAPIView):
    queryset = PlantPart.objects.all()
    serializer_class = PlantPartSerializer

class PlantPartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantPart.objects.all()
    serializer_class = PlantPartSerializer

class DiseaseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class DiseaseImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = DiseaseImage.objects.all()
    serializer_class = DiseaseImageSerializer

class DiseaseImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiseaseImage.objects.all()
    serializer_class = DiseaseImageSerializer

class EuropeanDiseaseListCreateAPIView(generics.ListCreateAPIView):
    queryset = EuropeanDisease.objects.all()
    serializer_class = EuropeanDiseaseSerializer

class EuropeanDiseaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EuropeanDisease.objects.all()
    serializer_class = EuropeanDiseaseSerializer

class PlantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer