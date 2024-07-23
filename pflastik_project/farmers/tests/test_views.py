# farmers/api/tests/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import (
    MonitoringData,
    MonitoringAlert,
    MonitoringAction,
    ForumPost,
    ForumComment,
    SeasonAlert,
    EnvironmentalCondition,
    CareTip,
    FinancialAid
)
from API.serializers import (
    MonitoringDataSerializer,
    MonitoringAlertSerializer,
    MonitoringActionSerializer,
    ForumPostSerializer,
    ForumCommentSerializer,
    SeasonAlertSerializer,
    EnvironmentalConditionSerializer,
    CareTipSerializer,
    FinancialAidSerializer
)

class APITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create test data
        self.monitoring_data = MonitoringData.objects.create(
            temperature=25.0, 
            humidity=50.0, 
            soil_moisture=30.0
        )
        self.monitoring_alert = MonitoringAlert.objects.create(
            alert_type='Test Alert',
            alert_message='This is a test alert message.'
        )
        self.monitoring_action = MonitoringAction.objects.create(name='Test Action')
        self.forum_post = ForumPost.objects.create(
            user=self.user,
            title='Test Post',
            content='This is a test forum post.'
        )
        self.forum_comment = ForumComment.objects.create(
            post=self.forum_post,
            user=self.user,
            content='This is a test comment.'
        )
        self.season_alert = SeasonAlert.objects.create(
            crop='Test Crop',
            alert_type='Test Season Alert',
            alert_message='This is a test season alert message.'
        )
        self.environmental_condition = EnvironmentalCondition.objects.create(
            temperature=25.0,
            humidity=50.0,
            soil_moisture=30.0,
            alert_message='This is a test alert.'
        )
        self.care_tip = CareTip.objects.create(
            crop='Test Crop',
            region='Test Region',
            tip='This is a test care tip.'
        )
        self.financial_aid = FinancialAid.objects.create(
            crop='Test Crop',
            price=100.00,
            transaction_date='2024-01-01'
        )

    # MonitoringData tests
    def test_monitoring_data_list_create_view(self):
        url = reverse('monitoringdata-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['temperature'], self.monitoring_data.temperature)
        
        response = self.client.post(url, {'temperature': 26.0, 'humidity': 55.0, 'soil_moisture': 35.0})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_monitoring_data_detail_view(self):
        url = reverse('monitoringdata-detail', args=[self.monitoring_data.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['temperature'], self.monitoring_data.temperature)
        
        response = self.client.put(url, {'temperature': 27.0, 'humidity': 60.0, 'soil_moisture': 40.0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.monitoring_data.refresh_from_db()
        self.assertEqual(self.monitoring_data.temperature, 27.0)
        
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MonitoringData.objects.filter(id=self.monitoring_data.id).exists())

    # MonitoringAlert tests
    def test_monitoring_alert_list_create_view(self):
        url = reverse('monitoringalert-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['alert_type'], self.monitoring_alert.alert_type)

        response = self.client.post(url, {'alert_type': 'New Alert', 'alert_message': 'New alert message.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_monitoring_alert_detail_view(self):
        url = reverse('monitoringalert-detail', args=[self.monitoring_alert.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['alert_type'], self.monitoring_alert.alert_type)

        response = self.client.put(url, {'alert_type': 'Updated Alert', 'alert_message': 'Updated alert message.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.monitoring_alert.refresh_from_db()
        self.assertEqual(self.monitoring_alert.alert_type, 'Updated Alert')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MonitoringAlert.objects.filter(id=self.monitoring_alert.id).exists())

    # MonitoringAction tests
    def test_monitoring_action_list_create_view(self):
        url = reverse('monitoringaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.monitoring_action.name)

        response = self.client.post(url, {'name': 'New Action'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_monitoring_action_detail_view(self):
        url = reverse('monitoringaction-detail', args=[self.monitoring_action.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.monitoring_action.name)

        response = self.client.put(url, {'name': 'Updated Action'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.monitoring_action.refresh_from_db()
        self.assertEqual(self.monitoring_action.name, 'Updated Action')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MonitoringAction.objects.filter(id=self.monitoring_action.id).exists())

    # ForumPost tests
    def test_forum_post_list_create_view(self):
        url = reverse('forumpost-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.forum_post.title)

        response = self.client.post(url, {'user': self.user.id, 'title': 'New Post', 'content': 'New post content.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_forum_post_detail_view(self):
        url = reverse('forumpost-detail', args=[self.forum_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.forum_post.title)

        response = self.client.put(url, {'user': self.user.id, 'title': 'Updated Post', 'content': 'Updated post content.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.forum_post.refresh_from_db()
        self.assertEqual(self.forum_post.title, 'Updated Post')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ForumPost.objects.filter(id=self.forum_post.id).exists())

    # ForumComment tests
    def test_forum_comment_list_create_view(self):
        url = reverse('forumcomment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], self.forum_comment.content)

        response = self.client.post(url, {'post': self.forum_post.id, 'user': self.user.id, 'content': 'New comment.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_forum_comment_detail_view(self):
        url = reverse('forumcomment-detail', args=[self.forum_comment.id])
        response = self.client.get(url)# farmers/api/tests/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import (
    MonitoringData,
    MonitoringAlert,
    MonitoringAction,
    ForumPost,
    ForumComment,
    SeasonAlert,
    EnvironmentalCondition,
    CareTip,
    FinancialAid
)
from serializers import (
    MonitoringDataSerializer,
    MonitoringAlertSerializer,
    MonitoringActionSerializer,
    ForumPostSerializer,
    ForumCommentSerializer,
    SeasonAlertSerializer,
    EnvironmentalConditionSerializer,
    CareTipSerializer,
    FinancialAidSerializer
)

class APITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create test data
        self.monitoring_data = MonitoringData.objects.create(
            temperature=25.0, 
            humidity=50.0, 
            soil_moisture=30.0
        )
        self.monitoring_alert = MonitoringAlert.objects.create(
            alert_type='Test Alert',
            alert_message='This is a test alert message.'
        )
        self.monitoring_action = MonitoringAction.objects.create(name='Test Action')
        self.forum_post = ForumPost.objects.create(
            user=self.user,
            title='Test Post',
            content='This is a test forum post.'
        )
        self.forum_comment = ForumComment.objects.create(
            post=self.forum_post,
            user=self.user,
            content='This is a test comment.'
        )
        self.season_alert = SeasonAlert.objects.create(
            crop='Test Crop',
            alert_type='Test Season Alert',
            alert_message='This is a test season alert message.'
        )
        self.environmental_condition = EnvironmentalCondition.objects.create(
            temperature=25.0,
            humidity=50.0,
            soil_moisture=30.0,
            alert_message='This is a test alert.'
        )
        self.care_tip = CareTip.objects.create(
            crop='Test Crop',
            region='Test Region',
            tip='This is a test care tip.'
        )
        self.financial_aid = FinancialAid.objects.create(
            crop='Test Crop',
            price=100.00,
            transaction_date='2024-01-01'
        )

    def test_monitoring_data_list_create_view(self):
        url = reverse('monitoringdata-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['temperature'], self.monitoring_data.temperature)
        
        response = self.client.post(url, {'temperature': 26.0, 'humidity': 55.0, 'soil_moisture': 35.0})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_monitoring_data_detail_view(self):
        url = reverse('monitoringdata-detail', args=[self.monitoring_data.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['temperature'], self.monitoring_data.temperature)
        
        response = self.client.put(url, {'temperature': 27.0, 'humidity': 60.0, 'soil_moisture': 40.0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.monitoring_data.refresh_from_db()
        self.assertEqual(self.monitoring_data.temperature, 27.0)
        
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MonitoringData.objects.filter(id=self.monitoring_data.id).exists())

    # Repeat similar tests for MonitoringAlert, MonitoringAction, ForumPost, ForumComment, SeasonAlert, EnvironmentalCondition, CareTip, and FinancialAid views

    def test_monitoring_alert_list_create_view(self):
        url = reverse('monitoringalert-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['alert_type'], self.monitoring_alert.alert_type)

        response = self.client.post(url, {'alert_type': 'New Alert', 'alert_message': 'New alert message.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_monitoring_alert_detail_view(self):
        url = reverse('monitoringalert-detail', args=[self.monitoring_alert.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['alert_type'], self.monitoring_alert.alert_type)

        response = self.client.put(url, {'alert_type': 'Updated Alert', 'alert_message': 'Updated alert message.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.monitoring_alert.refresh_from_db()
        self.assertEqual(self.monitoring_alert.alert_type, 'Updated Alert')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MonitoringAlert.objects.filter(id=self.monitoring_alert.id).exists())

    # Continue similarly for MonitoringAction, ForumPost, ForumComment, SeasonAlert, EnvironmentalCondition, CareTip, and FinancialAid

    # Add additional test methods for each of the other views as needed.

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.forum_comment.content)

        response = self.client.put(url, {'post': self.forum_post.id, 'user': self.user.id, 'content': 'Updated comment.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.forum_comment.refresh_from_db()
        self.assertEqual(self.forum_comment.content, 'Updated comment.')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ForumComment.objects.filter(id=self.forum_comment.id).exists())

    # SeasonAlert tests
    def test_season_alert_list_create_view(self):
        url = reverse('seasonalert-list')
        response = self
