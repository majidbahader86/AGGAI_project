from rest_framework import serializers
from .models import Profile, Foo
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'is_farmer', 'is_scientist']

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.is_farmer = validated_data.get('is_farmer', instance.is_farmer)
        instance.is_scientist = validated_data.get('is_scientist', instance.is_scientist)
        instance.save()
        return instance

class FooSerializer(serializers.ModelSerializer):
    user_display = serializers.CharField(source='get_user_display', read_only=True)

    class Meta:
        model = Foo
        fields = ['id', 'user', 'user_display']

    def create(self, validated_data):
        return Foo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance