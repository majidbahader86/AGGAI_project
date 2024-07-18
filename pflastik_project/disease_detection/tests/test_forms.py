# disease_detection/tests/test_forms.py

import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from disease_detection.models import DiseaseIdentificationRequest
from disease_detection.forms import DiseaseIdentificationRequestForm

@pytest.mark.django_db
def test_valid_form():
    user = User.objects.create_user(username='testuser', password='12345')
    disease_request = DiseaseIdentificationRequest.objects.create(
        user=user,
        request_time=timezone.now(),
        ai_requested=False
    )
    data = {
        'image': None,
        'ai_requested': True,
    }
    form = DiseaseIdentificationRequestForm(data=data)
    assert form.is_valid()
    disease_request = form.save(commit=False)
    disease_request.user = user
    disease_request.save()

    assert disease_request.ai_requested is True
    assert disease_request.image is None

@pytest.mark.django_db
def test_invalid_form():
    data = {
        'ai_requested': True,
    }
    form = DiseaseIdentificationRequestForm(data=data)
    assert not form.is_valid()
    assert 'image' in form.errors

@pytest.mark.django_db
def test_form_initial_data():
    user = User.objects.create_user(username='testuser', password='12345')
    disease_request = DiseaseIdentificationRequest.objects.create(
        user=user,
        request_time=timezone.now(),
        ai_requested=True
    )
    form = DiseaseIdentificationRequestForm(instance=disease_request)

    assert form.initial['ai_requested'] is True
    assert form.initial['image'] is None

@pytest.mark.django_db
def test_form_update():
    user = User.objects.create_user(username='testuser', password='12345')
    disease_request = DiseaseIdentificationRequest.objects.create(
        user=user,
        request_time=timezone.now(),
        ai_requested=False
    )
    data = {
        'ai_requested': True,
    }
    form = DiseaseIdentificationRequestForm(data=data, instance=disease_request)
    assert form.is_valid()
    updated_disease_request = form.save()

    assert updated_disease_request.ai_requested is True
    assert updated_disease_request.image is None
