# test_models.py
import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from disease_detection.models import DiseaseIdentificationRequest

@pytest.mark.django_db
def test_disease_identification_request_creation():
    # Create a user
    user = User.objects.create_user(username='testuser', password='12345')
    
    # Create a DiseaseIdentificationRequest instance
    request = DiseaseIdentificationRequest.objects.create(
        user=user,
        request_time=timezone.now(),
        ai_requested=True
    )
    
    # Check that the instance is created correctly
    assert request.user == user
    assert request.ai_requested is True
    assert request.image is None
    assert str(request) == f"Disease Identification Request by {user.username} at {request.request_time}"

@pytest.mark.django_db
def test_disease_identification_request_default_values():
    # Create a user
    user = User.objects.create_user(username='testuser2', password='12345')
    
    # Create a DiseaseIdentificationRequest instance with default values
    request = DiseaseIdentificationRequest.objects.create(
        user=user
    )
    
    # Check that default values are set correctly
    assert request.user == user
    assert request.ai_requested is False
    assert request.image is None
    assert request.request_time is not None
    assert str(request) == f"Disease Identification Request by {user.username} at {request.request_time}"

@pytest.mark.django_db
def test_disease_identification_request_image_field():
    # Create a user
    user = User.objects.create_user(username='testuser3', password='12345')
    
    # Create a DiseaseIdentificationRequest instance with an image
    with open('path/to/sample_image.jpg', 'rb') as img:
        request = DiseaseIdentificationRequest.objects.create(
            user=user,
            image=img,
            ai_requested=False
        )
    
    # Check that the image field is set correctly
    assert request.user == user
    assert request.image.name == 'disease_identification/sample_image.jpg'
    assert request.ai_requested is False
    assert str(request) == f"Disease Identification Request by {user.username} at {request.request_time}"
