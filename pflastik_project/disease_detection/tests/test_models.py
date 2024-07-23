from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from disease_detection.models import DiseaseIdentificationRequest

class DiseaseIdentificationRequestModelTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_disease_identification_request_creation(self):
        # Create a DiseaseIdentificationRequest instance
        disease_request = DiseaseIdentificationRequest.objects.create(
            user=self.user,
            ai_requested=True
        )

        # Verify the request was created successfully
        self.assertIsInstance(disease_request, DiseaseIdentificationRequest)
        self.assertEqual(disease_request.user.username, 'testuser')
        self.assertTrue(disease_request.ai_requested)
        self.assertIsNotNone(disease_request.request_time)

    def test_default_values(self):
        # Create a DiseaseIdentificationRequest instance without specifying ai_requested
        disease_request = DiseaseIdentificationRequest.objects.create(user=self.user)

        # Verify the default value of ai_requested
        self.assertFalse(disease_request.ai_requested)

    def test_str_representation(self):
        # Create a DiseaseIdentificationRequest instance
        disease_request = DiseaseIdentificationRequest.objects.create(
            user=self.user,
            ai_requested=False
        )

        # Check the string representation
        expected_str = f"Disease Identification Request by {self.user.username} at {disease_request.request_time}"
        self.assertEqual(str(disease_request), expected_str)

    def test_image_field_blank_and_null(self):
        # Create a DiseaseIdentificationRequest instance with image field as blank
        disease_request = DiseaseIdentificationRequest.objects.create(
            user=self.user,
            image=None
        )

        # Verify the image field can be blank and null
        self.assertIsNone(disease_request.image)

    def test_request_time_auto_now_add(self):
        # Create a DiseaseIdentificationRequest instance
        disease_request = DiseaseIdentificationRequest.objects.create(user=self.user)

        # Verify request_time is set automatically
        now = timezone.now()
        self.assertLess((now - disease_request.request_time).total_seconds(), 1)
