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


class DiseaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseImage
        fields = ['id', 'image', 'description']


class DiseaseSerializer(serializers.ModelSerializer):
    category = DiseaseCategorySerializer()
    affected_parts = PlantPartSerializer(many=True)
    images = DiseaseImageSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts', 'images']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        affected_parts_data = validated_data.pop('affected_parts')
        disease = Disease.objects.create(**validated_data)
        category = DiseaseCategory.objects.get_or_create(**category_data)[0]
        disease.category = category
        for part_data in affected_parts_data:
            part = PlantPart.objects.get_or_create(**part_data)[0]
            disease.affected_parts.add(part)
        return disease

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        affected_parts_data = validated_data.pop('affected_parts')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.symptoms = validated_data.get('symptoms', instance.symptoms)
        instance.treatment = validated_data.get('treatment', instance.treatment)
        instance.prevention = validated_data.get('prevention', instance.prevention)
        category = DiseaseCategory.objects.get_or_create(**category_data)[0]
        instance.category = category
        instance.affected_parts.clear()
        for part_data in affected_parts_data:
            part = PlantPart.objects.get_or_create(**part_data)[0]
            instance.affected_parts.add(part)
        instance.save()
        return instance


class EuropeanDiseaseSerializer(serializers.ModelSerializer):
    category = DiseaseCategorySerializer()
    affected_parts = PlantPartSerializer(many=True)

    class Meta:
        model = EuropeanDisease
        fields = ['id', 'name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        affected_parts_data = validated_data.pop('affected_parts')
        european_disease = EuropeanDisease.objects.create(**validated_data)
        category = DiseaseCategory.objects.get_or_create(**category_data)[0]
        european_disease.category = category
        for part_data in affected_parts_data:
            part = PlantPart.objects.get_or_create(**part_data)[0]
            european_disease.affected_parts.add(part)
        return european_disease

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        affected_parts_data = validated_data.pop('affected_parts')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.symptoms = validated_data.get('symptoms', instance.symptoms)
        instance.treatment = validated_data.get('treatment', instance.treatment)
        instance.prevention = validated_data.get('prevention', instance.prevention)
        category = DiseaseCategory.objects.get_or_create(**category_data)[0]
        instance.category = category
        instance.affected_parts.clear()
        for part_data in affected_parts_data:
            part = PlantPart.objects.get_or_create(**part_data)[0]
            instance.affected_parts.add(part)
        instance.save()
        return instance


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ['id', 'image', 'description', 'is_healthy']


class PlantSerializer(serializers.ModelSerializer):
    images = PlantImageSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = ['id', 'name', 'scientific_name', 'description', 'habitat', 'images']