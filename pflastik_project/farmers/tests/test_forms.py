# farmers/tests/test_forms.py

import pytest
from django.contrib.auth.models import User
from farmers.models import MonitoringData, MonitoringAction, MonitoringAlert, ForumPost, ForumComment, \
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
from farmers.forms import MonitoringDataForm, MonitoringAlertForm, MonitoringActionForm, \
    ForumPostForm, ForumCommentForm, SeasonAlertForm, EnvironmentalConditionForm, CareTipForm, FinancialAidForm, \
    FarmerSignupForm, FarmerLoginForm
from django.utils import timezone

@pytest.mark.django_db
def test_valid_monitoring_data_form():
    data = {
        'temperature': 25.5,
        'humidity': 55.0,
        'soil_moisture': 30.0
    }
    form = MonitoringDataForm(data=data)
    assert form.is_valid()
    monitoring_data = form.save()
    assert monitoring_data.temperature == 25.5
    assert monitoring_data.humidity == 55.0
    assert monitoring_data.soil_moisture == 30.0

@pytest.mark.django_db
def test_invalid_monitoring_data_form():
    data = {
        'temperature': 'invalid',  # Invalid data type
        'humidity': 55.0,
        'soil_moisture': 30.0
    }
    form = MonitoringDataForm(data=data)
    assert not form.is_valid()
    assert 'temperature' in form.errors

@pytest.mark.django_db
def test_valid_monitoring_alert_form():
    data = {
        'alert_type': 'Temperature Alert',
        'alert_message': 'High temperature detected.'
    }
    form = MonitoringAlertForm(data=data)
    assert form.is_valid()
    monitoring_alert = form.save()
    assert monitoring_alert.alert_type == 'Temperature Alert'
    assert monitoring_alert.alert_message == 'High temperature detected.'

@pytest.mark.django_db
def test_valid_monitoring_action_form():
    data = {
        'name': 'Watering'
    }
    form = MonitoringActionForm(data=data)
    assert form.is_valid()
    monitoring_action = form.save()
    assert monitoring_action.name == 'Watering'

@pytest.mark.django_db
def test_valid_forum_post_form():
    user = User.objects.create_user(username='testuser', password='12345')
    data = {
        'user': user.id,
        'title': 'Test Post',
        'content': 'This is a test post content.'
    }
    form = ForumPostForm(data=data)
    assert form.is_valid()
    forum_post = form.save()
    assert forum_post.user == user
    assert forum_post.title == 'Test Post'

@pytest.mark.django_db
def test_valid_forum_comment_form():
    user = User.objects.create_user(username='testuser', password='12345')
    forum_post = ForumPost.objects.create(user=user, title='Test Post', content='Test post content')
    data = {
        'post': forum_post.id,
        'user': user.id,
        'content': 'This is a test comment.'
    }
    form = ForumCommentForm(data=data)
    assert form.is_valid()
    forum_comment = form.save()
    assert forum_comment.post == forum_post
    assert forum_comment.user == user
    assert forum_comment.content == 'This is a test comment.'

@pytest.mark.django_db
def test_valid_season_alert_form():
    data = {
        'crop': 'Rice',
        'alert_type': 'Pest Infestation',
        'alert_message': 'Pest infestation detected in rice field.'
    }
    form = SeasonAlertForm(data=data)
    assert form.is_valid()
    season_alert = form.save()
    assert season_alert.crop == 'Rice'
    assert season_alert.alert_type == 'Pest Infestation'

@pytest.mark.django_db
def test_valid_environmental_condition_form():
    data = {
        'temperature': 28.5,
        'humidity': 60.0,
        'soil_moisture': 25.0,
        'alert_message': 'Dry conditions detected.'
    }
    form = EnvironmentalConditionForm(data=data)
    assert form.is_valid()
    environmental_condition = form.save()
    assert environmental_condition.temperature == 28.5
    assert environmental_condition.humidity == 60.0

@pytest.mark.django_db
def test_valid_care_tip_form():
    data = {
        'crop': 'Tomato',
        'region': 'North America',
        'tip': 'Water tomato plants regularly to maintain soil moisture.'
    }
    form = CareTipForm(data=data)
    assert form.is_valid()
    care_tip = form.save()
    assert care_tip.crop == 'Tomato'
    assert care_tip.region == 'North America'

@pytest.mark.django_db
def test_valid_financial_aid_form():
    data = {
        'crop': 'Corn',
        'price': 500.00,
        'transaction_date': timezone.now().date()
    }
    form = FinancialAidForm(data=data)
    assert form.is_valid()
    financial_aid = form.save()
    assert financial_aid.crop == 'Corn'
    assert financial_aid.price == 500.00
