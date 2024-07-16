# AI_tool/serializers.py

from rest_framework import serializers
from .models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'user', 'llm_name', 'timestamp', 'user_messages', 'llm_responses', 'context']

class AIToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AITool
        fields = ['id', 'name', 'description', 'model_file', 'usage_instructions']

class AIQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIQuestion
        fields = ['id', 'user', 'question', 'created_at']

class AIAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIAnswer
        fields = ['id', 'question', 'answer']

class AIToolUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIToolUsage
        fields = ['id', 'tool', 'user', 'input_data', 'result', 'usage_date']