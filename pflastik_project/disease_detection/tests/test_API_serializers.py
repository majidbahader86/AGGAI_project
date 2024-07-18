# disease_detection/tests/test_API_serializers.py

import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from disease_detection.models import DiseaseIdentificationRequest
from disease_detection.API.serializers import DiseaseIdentificationRequestSerializer

@pytest.mark.django_db
def test_serializer_serialization():
    user = User.objects.create_user(username='testuser', password='12345')
    request_instance = DiseaseIdentificationRequest.objects.create(
        user=user,
        request_time=timezone.now(),
        ai_requested=True
    )

    serializer = DiseaseIdentificationRequestSerializer(request_instance)
    data = serializer.data

    assert data['user'] == user.id
    assert data['ai_requested'] is True
    assert 'id' in data
    assert 'request_time' in data
    assert 'image' in data

@pytest.mark.django_db
def test_serializer_deserialization():
    user = User.objects.create_user(username='testuser', password='12345')
    data = {
        'user': user.id,
        'request_time': timezone.now(),
        'ai_requested': True,
        'image': None
    }

    serializer = DiseaseIdentificationRequestSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    request_instance = serializer.save()

    assert request_instance.user == user
    assert request_instance.ai_requested is True
    assert request_instance.image is None

@pytest.mark.django_db
def test_serializer_update():
    user = User.objects.create_user(username='testuser', password='12345')
    request_instance = DiseaseIdentificationRequest.objects.create(
        user=user,
        request_time=timezone.now(),
        ai_requested=False
    )

    new_data = {
        'user': user.id,
        'ai_requested': True
    }

    serializer = DiseaseIdentificationRequestSerializer(request_instance, data=new_data, partial=True)
    assert serializer.is_valid(), serializer.errors
    updated_instance = serializer.save()

    assert updated_instance.user == user
    assert updated_instance.ai_requested is True

@pytest.mark.django_db
def test_serializer_validation_error():
    data = {
        'request_time': timezone.now(),
        'ai_requested': True
    }

    serializer = DiseaseIdentificationRequestSerializer(data=data)
    assert not serializer.is_valid()
    assert 'user' in serializer.errors
