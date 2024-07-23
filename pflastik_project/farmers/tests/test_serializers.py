from django.test import TestCase
from django.contrib.auth.models import User
from farmers.models import (
    MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment,
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
)
from farmers.forms import (
    MonitoringDataForm, MonitoringAlertForm, MonitoringActionForm, ForumPostForm,
    ForumCommentForm, SeasonAlertForm, EnvironmentalConditionForm, CareTipForm,
    FinancialAidForm, FarmerSignupForm, FarmerLoginForm
)
from accounts.models import Profile

class FarmersFormsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(user=self.user, is_farmer=True)

    def test_monitoring_data_form(self):
        form_data = {'temperature': 25.0, 'humidity': 50.0, 'soil_moisture': 30.0}
        form = MonitoringDataForm(data=form_data)
        self.assertTrue(form.is_valid())
        monitoring_data = form.save()
        self.assertEqual(monitoring_data.temperature, 25.0)

    def test_monitoring_alert_form(self):
        form_data = {'alert_type': 'Temperature', 'alert_message': 'High temperature alert'}
        form = MonitoringAlertForm(data=form_data)
        self.assertTrue(form.is_valid())
        monitoring_alert = form.save()
        self.assertEqual(monitoring_alert.alert_type, 'Temperature')

    def test_monitoring_action_form(self):
        form_data = {'name': 'Watering'}
        form = MonitoringActionForm(data=form_data)
        self.assertTrue(form.is_valid())
        monitoring_action = form.save()
        self.assertEqual(monitoring_action.name, 'Watering')

    def test_forum_post_form(self):
        form_data = {'user': self.user.id, 'title': 'Test Post', 'content': 'This is a test post'}
        form = ForumPostForm(data=form_data)
        self.assertTrue(form.is_valid())
        forum_post = form.save()
        self.assertEqual(forum_post.title, 'Test Post')

    def test_forum_comment_form(self):
        forum_post = ForumPost.objects.create(user=self.user, title='Test Post', content='This is a test post')
        form_data = {'post': forum_post.id, 'user': self.user.id, 'content': 'This is a test comment'}
        form = ForumCommentForm(data=form_data)
        self.assertTrue(form.is_valid())
        forum_comment = form.save()
        self.assertEqual(forum_comment.content, 'This is a test comment')

    def test_season_alert_form(self):
        form_data = {'crop': 'Wheat', 'alert_type': 'Frost', 'alert_message': 'Frost alert'}
        form = SeasonAlertForm(data=form_data)
        self.assertTrue(form.is_valid())
        season_alert = form.save()
        self.assertEqual(season_alert.crop, 'Wheat')

    def test_environmental_condition_form(self):
        form_data = {'temperature': 25.0, 'humidity': 50.0, 'soil_moisture': 30.0}
        form = EnvironmentalConditionForm(data=form_data)
        self.assertTrue(form.is_valid())
        environmental_condition = form.save()
        self.assertEqual(environmental_condition.temperature, 25.0)

    def test_care_tip_form(self):
        form_data = {'crop': 'Wheat', 'region': 'Midwest', 'tip': 'Water regularly'}
        form = CareTipForm(data=form_data)
        self.assertTrue(form.is_valid())
        care_tip = form.save()
        self.assertEqual(care_tip.crop, 'Wheat')

    def test_financial_aid_form(self):
        form_data = {'crop': 'Wheat', 'price': 100.00, 'transaction_date': '2023-01-01'}
        form = FinancialAidForm(data=form_data)
        self.assertTrue(form.is_valid())
        financial_aid = form.save()
        self.assertEqual(financial_aid.price, 100.00)

    def test_farmer_signup_form(self):
        form_data = {
            'username': 'newfarmer', 'email': 'newfarmer@example.com',
            'password1': 'password123', 'password2': 'password123'
        }
        form = FarmerSignupForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(user.profile.is_farmer)

    def test_farmer_login_form(self):
        form_data = {'username': 'testuser', 'password': '12345'}
        form = FarmerLoginForm(data=form_data)
        self.assertTrue(form.is_valid())
