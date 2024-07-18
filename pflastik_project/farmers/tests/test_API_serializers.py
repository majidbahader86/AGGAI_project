# farmers/API/tests/test_serializers.py

import pytest
from datetime import datetime
from farmers.API.serializers import (
    MonitoringDataSerializer, MonitoringAlertSerializer, MonitoringActionSerializer,
    ForumPostSerializer, ForumCommentSerializer, SeasonAlertSerializer,
    EnvironmentalConditionSerializer, CareTipSerializer, FinancialAidSerializer
)
from farmers.models import MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment, \
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
from django.contrib.auth.models import User

@pytest.fixture
def sample_user():
    return User.objects.create(username='testuser', email='test@example.com')

@pytest.fixture
def sample_monitoring_data(sample_user):
    return MonitoringData.objects.create(
        user=sample_user,
        timestamp=datetime.now(),
        temperature=25.0,
        humidity=60.0,
        soil_moisture=40.0
    )

@pytest.fixture
def sample_monitoring_alert():
    return MonitoringAlert.objects.create(
        alert_type='Temperature Alert',
        alert_message='High temperature detected.'
    )

@pytest.mark.django_db
def test_monitoring_data_serializer():
    data = {
        'user': 1,  # Assuming user ID 1 exists
        'timestamp': datetime.now(),
        'temperature': 25.0,
        'humidity': 60.0,
        'soil_moisture': 40.0
    }
    serializer = MonitoringDataSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_monitoring_alert_serializer(sample_monitoring_alert):
    serializer = MonitoringAlertSerializer(sample_monitoring_alert)
    assert serializer.data['alert_type'] == 'Temperature Alert'

# Add similar tests for other serializers...
