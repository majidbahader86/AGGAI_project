# scientists/tests/test_serializers.py

import pytest
from django.contrib.auth.models import User
from scientists.models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from scientists.serializers import (
    PublicationSerializer, ForumPostSerializer, ForumCommentSerializer,
    ExpertSerializer, DiagnosticSessionSerializer, TutorialSerializer
)

@pytest.fixture
def sample_publication():
    return Publication.objects.create(
        title='Sample Publication',
        author='John Doe',
        abstract='Sample abstract',
        content='Sample content',
        published_date='2023-01-01',  # Replace with a valid date string
        category='Science',
        external_link='https://example.com'
    )

@pytest.fixture
def sample_forum_post(sample_user):
    return ForumPost.objects.create(
        user=sample_user,
        title='Sample Forum Post',
        content='Sample content'
    )

@pytest.fixture
def sample_forum_comment(sample_forum_post, sample_user):
    return ForumComment.objects.create(
        post=sample_forum_post,
        user=sample_user,
        content='Sample comment'
    )

@pytest.fixture
def sample_expert():
    return Expert.objects.create(
        name='John Smith',
        field_of_expertise='Botany',
        bio='Expert in plant sciences',
        contact_info='john.smith@example.com',
        photo=None  # Replace with an actual photo or None
    )

@pytest.fixture
def sample_diagnostic_session(sample_user):
    return DiagnosticSession.objects.create(
        user=sample_user,
        plant='Sample Plant',
        symptoms='Sample symptoms',
        diagnosis='Sample diagnosis'
    )

@pytest.fixture
def sample_tutorial():
    return Tutorial.objects.create(
        title='Sample Tutorial',
        content='Sample content',
        category='Science'
    )

@pytest.mark.django_db
def test_publication_serializer(sample_publication):
    serializer = PublicationSerializer(instance=sample_publication)
    assert serializer.data

@pytest.mark.django_db
def test_forum_post_serializer(sample_forum_post):
    serializer = ForumPostSerializer(instance=sample_forum_post)
    assert serializer.data

@pytest.mark.django_db
def test_forum_comment_serializer(sample_forum_comment):
    serializer = ForumCommentSerializer(instance=sample_forum_comment)
    assert serializer.data

@pytest.mark.django_db
def test_expert_serializer(sample_expert):
    serializer = ExpertSerializer(instance=sample_expert)
    assert serializer.data

@pytest.mark.django_db
def test_diagnostic_session_serializer(sample_diagnostic_session):
    serializer = DiagnosticSessionSerializer(instance=sample_diagnostic_session)
    assert serializer.data

@pytest.mark.django_db
def test_tutorial_serializer(sample_tutorial):
    serializer = TutorialSerializer(instance=sample_tutorial)
    assert serializer.data
