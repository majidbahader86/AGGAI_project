# farmers/tests/test_serializers.py

import pytest
from django.contrib.auth.models import User
from farmers.models import MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment, \
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
from farmers.serializers import MonitoringDataSerializer, MonitoringAlertSerializer, MonitoringActionSerializer, \
    ForumPostSerializer, ForumCommentSerializer, SeasonAlertSerializer, EnvironmentalConditionSerializer, \
    CareTipSerializer, FinancialAidSerializer
from datetime import datetime

@pytest.mark.django_db
def test_monitoring_data_serializer():
    monitoring_data = MonitoringData.objects.create(
        timestamp=datetime.now(),
        temperature=25.5,
        humidity=60.0,
        soil_moisture=35.0
    )
    serializer = MonitoringDataSerializer(monitoring_data)
    assert serializer.data['temperature'] == 25.5
    assert serializer.data['humidity'] == 60.0
    assert serializer.data['soil_moisture'] == 35.0

@pytest.mark.django_db
def test_monitoring_alert_serializer():
    monitoring_alert = MonitoringAlert.objects.create(
        alert_type='Temperature Alert',
        alert_message='High temperature detected.'
    )
    serializer = MonitoringAlertSerializer(monitoring_alert)
    assert serializer.data['alert_type'] == 'Temperature Alert'
    assert serializer.data['alert_message'] == 'High temperature detected.'

@pytest.mark.django_db
def test_monitoring_action_serializer():
    monitoring_action = MonitoringAction.objects.create(
        name='Watering'
    )
    serializer = MonitoringActionSerializer(monitoring_action)
    assert serializer.data['name'] == 'Watering'

@pytest.mark.django_db
def test_forum_post_serializer():
    user = User.objects.create_user(username='testuser', password='12345')
    forum_post = ForumPost.objects.create(
        user=user,
        title='Test Post',
        content='This is a test post content.'
    )
    serializer = ForumPostSerializer(forum_post)
    assert serializer.data['title'] == 'Test Post'
    assert serializer.data['content'] == 'This is a test post content.'

@pytest.mark.django_db
def test_forum_comment_serializer():
    user = User.objects.create_user(username='testuser', password='12345')
    forum_post = ForumPost.objects.create(
        user=user,
        title='Test Post',
        content='This is a test post content.'
    )
    forum_comment = ForumComment.objects.create(
        post=forum_post,
        user=user,
        content='This is a test comment.'
    )
    serializer = ForumCommentSerializer(forum_comment)
    assert serializer.data['content'] == 'This is a test comment.'

@pytest.mark.django_db
def test_season_alert_serializer():
    season_alert = SeasonAlert.objects.create(
        crop='Rice',
        alert_type='Pest Infestation',
        alert_message='Pest infestation detected in rice field.'
    )
    serializer = SeasonAlertSerializer(season_alert)
    assert serializer.data['crop'] == 'Rice'
    assert serializer.data['alert_type'] == 'Pest Infestation'

@pytest.mark.django_db
def test_environmental_condition_serializer():
    environmental_condition = EnvironmentalCondition.objects.create(
        timestamp=datetime.now(),
        temperature=28.5,
        humidity=60.0,
        soil_moisture=25.0,
        alert_message='Dry conditions detected.'
    )
    serializer = EnvironmentalConditionSerializer(environmental_condition)
    assert serializer.data['temperature'] == 28.5
    assert serializer.data['humidity'] == 60.0

@pytest.mark.django_db
def test_care_tip_serializer():
    care_tip = CareTip.objects.create(
        crop='Tomato',
        region='North America',
        tip='Water tomato plants regularly to maintain soil moisture.'
    )
    serializer = CareTipSerializer(care_tip)
    assert serializer.data['crop'] == 'Tomato'
    assert serializer.data['region'] == 'North America'

@pytest.mark.django_db
def test_financial_aid_serializer():
    financial_aid = FinancialAid.objects.create(
        crop='Corn',
        price=500.00,
        transaction_date=datetime.now().date()
    )
    serializer = FinancialAidSerializer(financial_aid)
    assert serializer.data['crop'] == 'Corn'
    assert serializer.data['price'] == '500.00'  # DecimalField is serialized as string
