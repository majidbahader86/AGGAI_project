from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import serializers
from disease_detection.models import DiseaseIdentificationRequest
from ..serializers import DiseaseIdentificationRequestSerializer

class DiseaseIdentificationRequestSerializerTest(APITestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a DiseaseIdentificationRequest instance for testing
        self.disease_request = DiseaseIdentificationRequest.objects.create(
            user=self.user,
            ai_requested=True
        )

    def test_serializer_contains_expected_fields(self):
        serializer = DiseaseIdentificationRequestSerializer(instance=self.disease_request)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'user', 'request_time', 'image', 'ai_requested']))

    def test_serializer_data(self):
        serializer = DiseaseIdentificationRequestSerializer(instance=self.disease_request)
        data = serializer.data
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['ai_requested'], True)
        self.assertIsNone(data['image'])  # Assuming no image was provided

    def test_serializer_create(self):
        data = {
            'user': self.user.id,
            'ai_requested': False
        }
        serializer = DiseaseIdentificationRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        disease_request = serializer.save()

        self.assertEqual(disease_request.user, self.user)
        self.assertEqual(disease_request.ai_requested, False)
        self.assertIsNotNone(disease_request.request_time)

    def test_serializer_update(self):
        data = {
            'user': self.user.id,
            'ai_requested': False
        }
        serializer = DiseaseIdentificationRequestSerializer(instance=self.disease_request, data=data)
        self.assertTrue(serializer.is_valid())
        disease_request = serializer.save()

        self.assertEqual(disease_request.user, self.user)
        self.assertEqual(disease_request.ai_requested, False)

    def test_invalid_serializer(self):
        # Missing required fields
        data = {}
        serializer = DiseaseIdentificationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('user', serializer.errors)
        self.assertIn('ai_requested', serializer.errors)

# The below lines ensure the tests are executed as part of the test suite
if __name__ == "__main__":
    TestCase.main()
