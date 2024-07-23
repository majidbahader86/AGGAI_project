from rest_framework import viewsets
from .models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage
from .serializers import ConversationSerializer, AIToolSerializer, AIQuestionSerializer, AIAnswerSerializer, AIToolUsageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class AIToolViewSet(viewsets.ModelViewSet):
    queryset = AITool.objects.all()
    serializer_class = AIToolSerializer

class AIQuestionViewSet(viewsets.ModelViewSet):
    queryset = AIQuestion.objects.all()
    serializer_class = AIQuestionSerializer

class AIAnswerViewSet(viewsets.ModelViewSet):
    queryset = AIAnswer.objects.all()
    serializer_class = AIAnswerSerializer

class AIToolUsageViewSet(viewsets.ModelViewSet):
    queryset = AIToolUsage.objects.all()
    serializer_class = AIToolUsageSerializer
