from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile, Foo

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user, is_farmer=True)

    def test_profile_creation(self):
        """Test profile is created correctly"""
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertTrue(self.profile.is_farmer)
        self.assertFalse(self.profile.is_scientist)

    def test_profile_update(self):
        """Test updating profile fields"""
        self.profile.is_scientist = True
        self.profile.save()
        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertTrue(updated_profile.is_scientist)

class FooModelTest(TestCase):

    def setUp(self):
        self.foo = Foo.objects.create(user='F')

    def test_foo_creation(self):
        """Test foo is created correctly"""
        self.assertEqual(str(self.foo), 'Farmer')

    def test_foo_update(self):
        """Test updating foo instance"""
        self.foo.user = 'S'
        self.foo.save()
        updated_foo = Foo.objects.get(id=self.foo.id)
        self.assertEqual(str(updated_foo), 'Scientist')

    def test_foo_choices(self):
        """Test user choices in Foo model"""
        choices = dict(Foo.USER_CHOICES)
        self.assertEqual(choices['S'], 'Scientist')
        self.assertEqual(choices['F'], 'Farmer')

    def test_signal_create_profile(self):
        """Test signal creates profile for new user"""
        new_user = User.objects.create(username='newuser')
        self.assertTrue(Profile.objects.filter(user=new_user).exists())

    def test_signal_update_profile(self):
        """Test signal updates existing profile for user"""
        self.user = User.objects.create(username='existinguser')
        self.user.profile.is_farmer = True
        self.user.save()
        updated_profile = Profile.objects.get(user=self.user)
        self.assertTrue(updated_profile.is_farmer)


