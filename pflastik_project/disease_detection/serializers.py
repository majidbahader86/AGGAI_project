# disease_detection/serializers.py

from rest_framework import serializers
from .models import DiseaseIdentificationRequest

class DiseaseIdentificationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseIdentificationRequest
        fields = ['id', 'user', 'request_time', 'image', 'ai_requested']

    def create(self, validated_data):
        return DiseaseIdentificationRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.request_time = validated_data.get('request_time', instance.request_time)
        instance.image = validated_data.get('image', instance.image)
        instance.ai_requested = validated_data.get('ai_requested', instance.ai_requested)
        instance.save()
        return instance