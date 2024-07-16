# farmers/serializers.py

from rest_framework import serializers
from .models import MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment, SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
from django.contrib.auth.models import User as DjangoUser

class MonitoringDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringData
        fields = '__all__'

class MonitoringAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringAlert
        fields = '__all__'

class MonitoringActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringAction
        fields = '__all__'

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'

class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = '__all__'

class SeasonAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonAlert
        fields = '__all__'

class EnvironmentalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalCondition
        fields = '__all__'

class CareTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareTip
        fields = '__all__'

class FinancialAidSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAid
        fields = '__all__'