
from django.test import TestCase
from django.contrib.auth.models import User as DjangoUser
from farmers.models import (
    MonitoringData,
    MonitoringAlert,
    MonitoringAction,
    ForumPost,
    ForumComment,
    SeasonAlert,
    EnvironmentalCondition,
    CareTip,
    FinancialAid,
)
from datetime import datetime, timedelta

class MonitoringDataModelTest(TestCase):

    def setUp(self):
        self.data = MonitoringData.objects.create(
            temperature=25.5,
            humidity=40.0,
            soil_moisture=30.0
        )

    def test_monitoring_data_creation(self):
        self.assertTrue(isinstance(self.data, MonitoringData))
        self.assertEqual(self.data.__str__(), f"Monitoring Data at {self.data.timestamp}")

class MonitoringAlertModelTest(TestCase):

    def setUp(self):
        self.alert = MonitoringAlert.objects.create(
            alert_type="Temperature",
            alert_message="High temperature detected"
        )

    def test_monitoring_alert_creation(self):
        self.assertTrue(isinstance(self.alert, MonitoringAlert))
        self.assertEqual(self.alert.__str__(), f"Monitoring Alert - {self.alert.alert_type}")

class MonitoringActionModelTest(TestCase):

    def setUp(self):
        self.action = MonitoringAction.objects.create(
            name="Irrigation"
        )

    def test_monitoring_action_creation(self):
        self.assertTrue(isinstance(self.action, MonitoringAction))
        self.assertEqual(self.action.__str__(), self.action.name)

class ForumPostModelTest(TestCase):

    def setUp(self):
        self.user = DjangoUser.objects.create_user(username='testuser', password='12345')
        self.post = ForumPost.objects.create(
            user=self.user,
            title="Test Post",
            content="This is a test post."
        )

    def test_forum_post_creation(self):
        self.assertTrue(isinstance(self.post, ForumPost))
        self.assertEqual(self.post.__str__(), self.post.title)

class ForumCommentModelTest(TestCase):

    def setUp(self):
        self.user = DjangoUser.objects.create_user(username='testuser', password='12345')
        self.post = ForumPost.objects.create(
            user=self.user,
            title="Test Post",
            content="This is a test post."
        )
        self.comment = ForumComment.objects.create(
            post=self.post,
            user=self.user,
            content="This is a test comment."
        )

    def test_forum_comment_creation(self):
        self.assertTrue(isinstance(self.comment, ForumComment))
        self.assertEqual(self.comment.__str__(), f"Comment by {self.comment.user.username} on {self.comment.post.title}")

class SeasonAlertModelTest(TestCase):

    def setUp(self):
        self.alert = SeasonAlert.objects.create(
            crop="Wheat",
            alert_type="Pest",
            alert_message="Pest alert for wheat."
        )

    def test_season_alert_creation(self):
        self.assertTrue(isinstance(self.alert, SeasonAlert))
        self.assertEqual(self.alert.__str__(), f"{self.alert.crop} Alert - {self.alert.alert_type}")

class EnvironmentalConditionModelTest(TestCase):

    def setUp(self):
        self.condition = EnvironmentalCondition.objects.create(
            temperature=25.5,
            humidity=40.0,
            soil_moisture=30.0,
            alert_message="Optimal conditions."
        )

    def test_environmental_condition_creation(self):
        self.assertTrue(isinstance(self.condition, EnvironmentalCondition))
        self.assertEqual(self.condition.__str__(), f"Environmental Condition at {self.condition.timestamp}")

class CareTipModelTest(TestCase):

    def setUp(self):
        self.tip = CareTip.objects.create(
            crop="Wheat",
            region="North",
            tip="Water regularly during dry seasons."
        )

    def test_care_tip_creation(self):
        self.assertTrue(isinstance(self.tip, CareTip))
        self.assertEqual(self.tip.__str__(), f"Care Tip for {self.tip.crop} in {self.tip.region}")

class FinancialAidModelTest(TestCase):

    def setUp(self):
        self.aid = FinancialAid.objects.create(
            crop="Wheat",
            price=1000.00,
            transaction_date=datetime.now().date() - timedelta(days=1)
        )

    def test_financial_aid_creation(self):
        self.assertTrue(isinstance(self.aid, FinancialAid))
        self.assertEqual(self.aid.__str__(), f"{self.aid.crop} - {self.aid.transaction_date}")

