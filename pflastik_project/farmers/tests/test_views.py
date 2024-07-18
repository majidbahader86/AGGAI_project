# farmers/tests/test_views.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from farmers.models import MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment, \
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid

@pytest.fixture
def logged_in_client():
    user = User.objects.create_user(username='testuser', password='12345')
    client = Client()
    client.force_login(user)
    return client

@pytest.mark.django_db
def test_farmer_signup_view(client):
    response = client.get(reverse('farmer_signup'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_farmer_signup_form_submit(client):
    data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'newpassword',
        'password2': 'newpassword'
    }
    response = client.post(reverse('farmer_signup'), data)
    assert response.status_code == 302  # Redirects upon successful signup

@pytest.mark.django_db
def test_farmer_login_view(client):
    response = client.get(reverse('farmer_login'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_farmer_login_form_submit(client):
    user = User.objects.create_user(username='testuser', password='12345')
    data = {
        'username': 'testuser',
        'password': '12345'
    }
    response = client.post(reverse('farmer_login'), data)
    assert response.status_code == 302  # Redirects upon successful login

@pytest.mark.django_db
def test_create_monitoring_data_view(logged_in_client):
    response = logged_in_client.get(reverse('create_monitoring_data'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_monitoring_alert_view(logged_in_client):
    response = logged_in_client.get(reverse('create_monitoring_alert'))
    assert response.status_code == 200


