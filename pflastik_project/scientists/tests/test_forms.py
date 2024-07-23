from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from scientists.forms import (
    PublicationForm, ForumPostForm, ForumCommentForm,
    ExpertForm, DiagnosticSessionForm, TutorialForm
)
from scientists.models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from django.contrib.auth.models import User
from plant_disease.models import PlantPart  # Ensure this import is correct based on your project structure

class PublicationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        
    def test_valid_form(self):
        form_data = {
            'title': 'Research Paper',
            'author': 'John Doe',
            'abstract': 'Abstract of the research paper',
            'content': 'Full content of the research paper',
            'published_date': '2024-07-23',
            'category': 'Research Paper',
            'external_link': 'https://example.com'
        }
        form_file = SimpleUploadedFile("test_file.pdf", b"file_content", content_type="application/pdf")
        form = PublicationForm(data=form_data, files={'file': form_file})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'title': '',
            'author': '',
            'abstract': '',
            'content': '',
            'published_date': '',
            'category': '',
            'external_link': ''
        }
        form = PublicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

class ForumPostFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_valid_form(self):
        form_data = {
            'title': 'Interesting Topic',
            'content': 'Details about the interesting topic',
        }
        form = ForumPostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'title': '',
            'content': ''
        }
        form = ForumPostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

class ForumCommentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = ForumPost.objects.create(user=self.user, title='Interesting Topic', content='Details about the interesting topic')

    def test_valid_form(self):
        form_data = {
            'content': 'This is a comment on the forum post.',
        }
        form = ForumCommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'content': ''
        }
        form = ForumCommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

class ExpertFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Dr. Jane Smith',
            'field_of_expertise': 'Botany',
            'bio': 'Expert in plant diseases.',
            'contact_info': 'jane.smith@example.com',
        }
        form_file = SimpleUploadedFile("expert_photo.jpg", b"file_content", content_type="image/jpeg")
        form = ExpertForm(data=form_data, files={'photo': form_file})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'name': '',
            'field_of_expertise': '',
            'bio': '',
            'contact_info': '',
        }
        form = ExpertForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

class DiagnosticSessionFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.plant = PlantPart.objects.create(name='Leaf')

    def test_valid_form(self):
        form_data = {
            'user': self.user.id,
            'plant': self.plant.id,
            'symptoms': 'Wilting leaves',
            'diagnosis': 'Possible fungal infection'
        }
        form = DiagnosticSessionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'user': '',
            'plant': '',
            'symptoms': '',
            'diagnosis': ''
        }
        form = DiagnosticSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)

class TutorialFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'title': 'Plant Care Basics',
            'content': 'Detailed guide on plant care.',
            'category': 'Plant Care'
        }
        form = TutorialForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'title': '',
            'content': '',
            'category': ''
        }
        form = TutorialForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 1)
