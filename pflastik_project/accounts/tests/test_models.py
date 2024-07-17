from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile, Foo

class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        user = User.objects.create(username='testuser')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertFalse(profile.is_farmer)
        self.assertFalse(profile.is_scientist)

class FooModelTest(TestCase):
    def test_foo_creation(self):
        foo = Foo.objects.create(user='S')
        self.assertEqual(foo.user, 'S')
        self.assertEqual(foo.__str__(), 'Scientist')

        foo = Foo.objects.create(user='F')
        self.assertEqual(foo.user, 'F')
        self.assertEqual(foo.__str__(), 'Farmer')

