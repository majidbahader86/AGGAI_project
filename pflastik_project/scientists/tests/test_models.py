from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from datetime import date
from plant_disease.models import PlantPart


class PublicationModelTest(TestCase):
    def setUp(self):
        self.publication = Publication.objects.create(
            title="Sample Publication",
            author="John Doe",
            abstract="Abstract of the publication",
            content="Full content of the publication",
            published_date=date.today(),
            category="Research Paper",
            file="path/to/file.pdf",
            external_link="http://example.com"
        )

    def test_publication_str(self):
        self.assertEqual(str(self.publication), "Sample Publication")

class ForumPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.forum_post = ForumPost.objects.create(
            user=self.user,
            title="Sample Forum Post",
            content="Content of the forum post"
        )

    def test_forum_post_str(self):
        self.assertEqual(str(self.forum_post), "Sample Forum Post")

class ForumCommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.forum_post = ForumPost.objects.create(
            user=self.user,
            title="Sample Forum Post",
            content="Content of the forum post"
        )
        self.forum_comment = ForumComment.objects.create(
            post=self.forum_post,
            user=self.user,
            content="This is a comment"
        )

    def test_forum_comment_str(self):
        self.assertEqual(str(self.forum_comment), "Comment by testuser on Sample Forum Post")

class ExpertModelTest(TestCase):
    def setUp(self):
        self.expert = Expert.objects.create(
            name="Dr. Smith",
            field_of_expertise="Plant Pathology",
            bio="Expert in plant diseases",
            contact_info="smith@example.com"
        )

    def test_expert_str(self):
        self.assertEqual(str(self.expert), "Dr. Smith")

class DiagnosticSessionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.plant = PlantPart.objects.create(name="Leaf")
        self.diagnostic_session = DiagnosticSession.objects.create(
            user=self.user,
            plant=self.plant,
            symptoms="Yellowing leaves",
            diagnosis="Fungal infection"
        )

    def test_diagnostic_session_str(self):
        self.assertEqual(str(self.diagnostic_session), "Diagnostic Session for Leaf by testuser")

class TutorialModelTest(TestCase):
    def setUp(self):
        self.tutorial = Tutorial.objects.create(
            title="Plant Care Basics",
            content="Content of the tutorial",
            category="Plant Care"
        )

    def test_tutorial_str(self):
        self.assertEqual(str(self.tutorial), "Plant Care Basics")
