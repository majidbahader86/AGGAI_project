from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Profile, Foo
from ..serializers import ProfileSerializer, FooSerializer

class ProfileAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.profile_data = {'user': 1, 'is_farmer': True, 'is_scientist': False}
        self.invalid_profile_data = {'user': 2}  # Incomplete data for validation errors
        self.profile = Profile.objects.create(user_id=1, is_farmer=True, is_scientist=False)

    def test_create_profile(self):
        response = self.client.post('/api/profiles/', self.profile_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_profile(self):
        response = self.client.post('/api/profiles/', self.invalid_profile_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_profiles(self):
        response = self.client.get('/api/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_profile(self):
        response = self.client.get('/api/profiles/{}/'.format(self.profile.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile(self):
        updated_data = {'user': 1, 'is_farmer': False, 'is_scientist': True}
        response = self.client.put('/api/profiles/{}/'.format(self.profile.id), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_profile(self):
        response = self.client.delete('/api/profiles/{}/'.format(self.profile.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FooAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.foo_data = {'user': 'F'}
        self.invalid_foo_data = {'user': 'X'}  # Invalid choice for user field
        self.foo = Foo.objects.create(user='F')

    def test_create_foo(self):
        response = self.client.post('/api/foos/', self.foo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_foo(self):
        response = self.client.post('/api/foos/', self.invalid_foo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_foos(self):
        response = self.client.get('/api/foos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_foo(self):
        response = self.client.get('/api/foos/{}/'.format(self.foo.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_foo(self):
        updated_data = {'user': 'S'}
        response = self.client.put('/api/foos/{}/'.format(self.foo.id), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_foo(self):
        response = self.client.delete('/api/foos/{}/'.format(self.foo.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
