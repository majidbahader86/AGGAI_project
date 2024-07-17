# accounts/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile, Foo
from accounts.forms import UserForm, ProfileForm, FooForm

class ViewsTestCase(TestCase):

    def setUp(self):
        # Create necessary objects for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user, is_farmer=True, is_scientist=False)
        self.foo = Foo.objects.create(user='F')

    def tearDown(self):
        # Clean up after each test
        self.user.delete()
        self.profile.delete()
        self.foo.delete()

    def test_index_view(self):
        # Test index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_profile_view(self):
        # Test profile view
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_update_user_view_get(self):
        # Test GET request for update_user view
        response = self.client.get(reverse('update_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_user.html')
        self.assertIsInstance(response.context['user_form'], UserForm)

    def test_update_user_view_post(self):
        # Test POST request for update_user view
        response = self.client.post(reverse('update_user', args=[self.user.id]), {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        })
        self.assertRedirects(response, reverse('profile_detail', args=[self.user.id]))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')

    def test_update_profile_view_get(self):
        # Test GET request for update_profile view
        response = self.client.get(reverse('update_profile', args=[self.profile.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_profile.html')
        self.assertIsInstance(response.context['profile_form'], ProfileForm)

    def test_update_profile_view_post(self):
        # Test POST request for update_profile view
        response = self.client.post(reverse('update_profile', args=[self.profile.id]), {
            'is_farmer': False,
            'is_scientist': True
        })
        self.assertRedirects(response, reverse('profile_detail', args=[self.user.id]))
        self.profile.refresh_from_db()
        self.assertFalse(self.profile.is_farmer)
        self.assertTrue(self.profile.is_scientist)

    def test_update_foo_view_get(self):
        # Test GET request for update_foo view
        response = self.client.get(reverse('update_foo', args=[self.foo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_foo.html')
        self.assertIsInstance(response.context['foo_form'], FooForm)

    def test_update_foo_view_post(self):
        # Test POST request for update_foo view
        response = self.client.post(reverse('update_foo', args=[self.foo.id]), {
            'user': 'S'
        })
        self.assertRedirects(response, reverse('foo_list'))
        self.foo.refresh_from_db()
        self.assertEqual(self.foo.user, 'S')

    

