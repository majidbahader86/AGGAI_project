# scientists/tests/test_forms.py

import pytest
from django.contrib.auth.models import User
from scientists.forms import (
    PublicationForm, ForumPostForm, ForumCommentForm, ExpertForm,
    DiagnosticSessionForm, TutorialForm, ScientistSignInForm, ScientistSignUpForm
)
from scientists.models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from django import forms

@pytest.fixture
def sample_user():
    return User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

@pytest.mark.django_db
def test_publication_form():
    form_data = {
        'title': 'Test Publication',
        'author': 'John Doe',
        'abstract': 'Test abstract',
        'content': 'Test content',
        'published_date': '2023-01-01',  # Replace with a valid date string
        'category': 'Science',
        'file': None,  # Replace with a FileField or None
        'external_link': 'https://example.com'
    }
    form = PublicationForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_forum_post_form(sample_user):
    form_data = {
        'user': sample_user.id,
        'title': 'Test Forum Post',
        'content': 'Test content'
    }
    form = ForumPostForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_forum_comment_form(sample_user):
    forum_post = ForumPost.objects.create(user=sample_user, title='Test Post', content='Test content')
    form_data = {
        'post': forum_post.id,
        'user': sample_user.id,
        'content': 'Test comment'
    }
    form = ForumCommentForm(data=form_data)
    assert form.is_valid()

# Add similar tests for other forms: ExpertForm, DiagnosticSessionForm, TutorialForm, ScientistSignInForm, ScientistSignUpForm
