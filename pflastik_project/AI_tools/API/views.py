from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    ConversationSerializer, 
    AIToolSerializer, 
    AIQuestionSerializer, 
    AIAnswerSerializer, 
    AIToolUsageSerializer
)
from ..models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

class AIToolViewSet(viewsets.ModelViewSet):
    queryset = AITool.objects.all()
    serializer_class = AIToolSerializer
    permission_classes = [permissions.IsAuthenticated]

class AIQuestionViewSet(viewsets.ModelViewSet):
    queryset = AIQuestion.objects.all()
    serializer_class = AIQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AIAnswerViewSet(viewsets.ModelViewSet):
    queryset = AIAnswer.objects.all()
    serializer_class = AIAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

class AIToolUsageViewSet(viewsets.ModelViewSet):
    queryset = AIToolUsage.objects.all()
    serializer_class = AIToolUsageSerializer
    permission_classes = [permissions.IsAuthenticated]
