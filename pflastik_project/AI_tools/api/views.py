from rest_framework import viewsets, permissions
from ..models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage
from .serializers import (
    ConversationSerializer, AIToolSerializer, AIQuestionSerializer,
    AIAnswerSerializer, AIToolUsageSerializer
)

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AIToolViewSet(viewsets.ModelViewSet):
    queryset = AITool.objects.all()
    serializer_class = AIToolSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AIQuestionViewSet(viewsets.ModelViewSet):
    queryset = AIQuestion.objects.all()
    serializer_class = AIQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AIAnswerViewSet(viewsets.ModelViewSet):
    queryset = AIAnswer.objects.all()
    serializer_class = AIAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

class AIToolUsageViewSet(viewsets.ModelViewSet):
    queryset = AIToolUsage.objects.all()
    serializer_class = AIToolUsageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
