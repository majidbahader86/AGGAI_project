from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from accounts.models import Profile, Foo

class IntegrationTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user, is_farmer=True, is_scientist=False)
        self.foo = Foo.objects.create(user='F')

    def test_api_endpoints(self):
        # Test API endpoints using APIClient
        url = reverse('api:user-detail', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Example of POST request to create a new Foo instance
        create_url = reverse('api:foo-list')
        data = {'user': 'S'}
        response = self.client.post(create_url, data)
        self.assertEqual(response.status_code, 201)  # Assuming successful creation

    def test_workflow(self):
        # Simulate a user workflow
        login_url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(login_url, data, format='json')
        self.assertEqual(response.status_code, 200)

        # Assuming authenticated, test interaction between views
        update_url = reverse('update_profile', args=[self.profile.id])
        update_data = {'is_farmer': False, 'is_scientist': True}
        response = self.client.post(update_url, update_data)
        self.assertEqual(response.status_code, 302)  # Redirect after update

    def tearDown(self):
        self.user.delete()
        self.profile.delete()
        self.foo.delete()
