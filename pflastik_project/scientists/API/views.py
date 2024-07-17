# scientists/api/views.py
from rest_framework import generics
from ..models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from .serializers import (
    PublicationSerializer, ForumPostSerializer, ForumCommentSerializer,
    ExpertSerializer, DiagnosticSessionSerializer, TutorialSerializer,
)

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class PublicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class ForumPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class ForumPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class ForumCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer

class ForumCommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer

class ExpertListCreateAPIView(generics.ListCreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer

class ExpertRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer

class DiagnosticSessionListCreateAPIView(generics.ListCreateAPIView):
    queryset = DiagnosticSession.objects.all()
    serializer_class = DiagnosticSessionSerializer

class DiagnosticSessionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiagnosticSession.objects.all()
    serializer_class = DiagnosticSessionSerializer

class TutorialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class TutorialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
