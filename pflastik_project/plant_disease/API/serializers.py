from rest_framework import serializers
from ..models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant, PlantImage

class DiseaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseCategory
        fields = ['id', 'name', 'description']

class PlantPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantPart
        fields = ['id', 'name']

class DiseaseSerializer(serializers.ModelSerializer):
    affected_parts = PlantPartSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']

class DiseaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseImage
        fields = ['id', 'disease', 'image', 'description']

class EuropeanDiseaseSerializer(serializers.ModelSerializer):
    affected_parts = PlantPartSerializer(many=True, read_only=True)

    class Meta:
        model = EuropeanDisease
        fields = ['id', 'name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'scientific_name', 'description', 'habitat']

class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ['id', 'plant', 'image', 'description', 'is_healthy']
