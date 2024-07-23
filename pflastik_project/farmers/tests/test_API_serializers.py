import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from farmers.models import (
    MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment,
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
)
from farmers.API.serializers import (
    MonitoringDataSerializer, MonitoringAlertSerializer, MonitoringActionSerializer,
    ForumPostSerializer, ForumCommentSerializer, SeasonAlertSerializer,
    EnvironmentalConditionSerializer, CareTipSerializer, FinancialAidSerializer
)

class APISerializersTest(TestCase):

    def setUp(self):
        # Create a test user for relations
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_monitoring_data_serializer(self):
        data = {'temperature': 25.0, 'humidity': 50.0, 'soil_moisture': 30.0}
        serializer = MonitoringDataSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        monitoring_data = serializer.save()
        self.assertEqual(monitoring_data.temperature, 25.0)
        self.assertEqual(monitoring_data.humidity, 50.0)
        self.assertEqual(monitoring_data.soil_moisture, 30.0)

    def test_monitoring_alert_serializer(self):
        data = {'alert_type': 'Temperature', 'alert_message': 'High temperature alert'}
        serializer = MonitoringAlertSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        monitoring_alert = serializer.save()
        self.assertEqual(monitoring_alert.alert_type, 'Temperature')
        self.assertEqual(monitoring_alert.alert_message, 'High temperature alert')

    def test_monitoring_action_serializer(self):
        data = {'name': 'Watering'}
        serializer = MonitoringActionSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        monitoring_action = serializer.save()
        self.assertEqual(monitoring_action.name, 'Watering')

    def test_forum_post_serializer(self):
        data = {'user': self.user.id, 'title': 'Test Post', 'content': 'This is a test post'}
        serializer = ForumPostSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        forum_post = serializer.save()
        self.assertEqual(forum_post.title, 'Test Post')
        self.assertEqual(forum_post.content, 'This is a test post')

    def test_forum_comment_serializer(self):
        forum_post = ForumPost.objects.create(user=self.user, title='Test Post', content='This is a test post')
        data = {'post': forum_post.id, 'user': self.user.id, 'content': 'This is a test comment'}
        serializer = ForumCommentSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        forum_comment = serializer.save()
        self.assertEqual(forum_comment.content, 'This is a test comment')

    def test_season_alert_serializer(self):
        data = {'crop': 'Wheat', 'alert_type': 'Frost', 'alert_message': 'Frost alert'}
        serializer = SeasonAlertSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        season_alert = serializer.save()
        self.assertEqual(season_alert.crop, 'Wheat')
        self.assertEqual(season_alert.alert_type, 'Frost')

    def test_environmental_condition_serializer(self):
        data = {'temperature': 25.0, 'humidity': 50.0, 'soil_moisture': 30.0}
        serializer = EnvironmentalConditionSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        environmental_condition = serializer.save()
        self.assertEqual(environmental_condition.temperature, 25.0)
        self.assertEqual(environmental_condition.humidity, 50.0)
        self.assertEqual(environmental_condition.soil_moisture, 30.0)

    def test_care_tip_serializer(self):
        data = {'crop': 'Wheat', 'region': 'Midwest', 'tip': 'Water regularly'}
        serializer = CareTipSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        care_tip = serializer.save()
        self.assertEqual(care_tip.crop, 'Wheat')
        self.assertEqual(care_tip.region, 'Midwest')

    def test_financial_aid_serializer(self):
        data = {'crop': 'Wheat', 'price': 100.00, 'transaction_date': '2023-01-01'}
        serializer = FinancialAidSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        financial_aid = serializer.save()
        self.assertEqual(financial_aid.crop, 'Wheat')
        self.assertEqual(financial_aid.price, 100.00)

if __name__ == "__main__":
    unittest.main()
