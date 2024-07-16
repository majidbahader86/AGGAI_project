from rest_framework import serializers
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'author', 'abstract', 'content', 'published_date', 'category', 'file', 'external_link']


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id', 'user', 'title', 'content', 'created_at']


class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = ['id', 'post', 'user', 'content', 'created_at']


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ['id', 'name', 'field_of_expertise', 'bio', 'contact_info', 'photo']


class DiagnosticSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticSession
        fields = ['id', 'user', 'plant', 'symptoms', 'diagnosis', 'created_at']


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'category']