from django.test import TestCase
from ..models import Profile, Foo
from ..serializers import ProfileSerializer, FooSerializer
from django.contrib.auth.models import User

class ProfileSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile_data = {
            'user': self.user,
            'is_farmer': True,
            'is_scientist': False
        }

    def test_profile_serializer_create(self):
        serializer = ProfileSerializer(data=self.profile_data)
        self.assertTrue(serializer.is_valid())
        profile = serializer.save()
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.is_farmer, True)
        self.assertEqual(profile.is_scientist, False)

    def test_profile_serializer_update(self):
        profile = Profile.objects.create(user=self.user, is_farmer=False, is_scientist=True)
        updated_data = {
            'is_farmer': True,
            'is_scientist': False
        }
        serializer = ProfileSerializer(instance=profile, data=updated_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_profile = serializer.save()
        self.assertEqual(updated_profile.user, self.user)
        self.assertEqual(updated_profile.is_farmer, True)
        self.assertEqual(updated_profile.is_scientist, False)

class FooSerializerTest(TestCase):
    def setUp(self):
        self.foo_data = {
            'user': 'F'
        }

    def test_foo_serializer_create(self):
        serializer = FooSerializer(data=self.foo_data)
        self.assertTrue(serializer.is_valid())
        foo = serializer.save()
        self.assertEqual(foo.user, 'F')

    def test_foo_serializer_update(self):
        foo = Foo.objects.create(user='S')
        updated_data = {
            'user': 'F'
        }
        serializer = FooSerializer(instance=foo, data=updated_data)
        self.assertTrue(serializer.is_valid())
        updated_foo = serializer.save()
        self.assertEqual(updated_foo.user, 'F')
