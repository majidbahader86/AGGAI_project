from django.urls import path
from .views import (conversation_list, conversation_detail, create_conversation, update_conversation, delete_conversation,
                    ai_tool_list, ai_tool_detail, create_ai_tool, update_ai_tool, delete_ai_tool,
                    ai_question_list, ai_question_detail, create_ai_question, update_ai_question, delete_ai_question,
                    ai_answer_list, ai_answer_detail, create_ai_answer, update_ai_answer, delete_ai_answer,
                    ai_tool_usage_list, ai_tool_usage_detail, create_ai_tool_usage, update_ai_tool_usage, delete_ai_tool_usage)

urlpatterns = [
    path('conversations/', conversation_list, name='conversation-list'),
    path('conversations/<int:pk>/', conversation_detail, name='conversation-detail'),
    path('conversations/create/', create_conversation, name='create-conversation'),
    path('conversations/<int:pk>/update/', update_conversation, name='update-conversation'),
    path('conversations/<int:pk>/delete/', delete_conversation, name='delete-conversation'),

    path('ai_tools/', ai_tool_list, name='ai_tool-list'),
    path('ai_tools/<int:pk>/', ai_tool_detail, name='ai_tool-detail'),
    path('ai_tools/create/', create_ai_tool, name='create-ai-tool'),
    path('ai_tools/<int:pk>/update/', update_ai_tool, name='update-ai-tool'),
    path('ai_tools/<int:pk>/delete/', delete_ai_tool, name='delete-ai-tool'),

    path('ai_questions/', ai_question_list, name='ai_question-list'),
    path('ai_questions/<int:pk>/', ai_question_detail, name='ai_question-detail'),
    path('ai_questions/create/', create_ai_question, name='create-ai-question'),
    path('ai_questions/<int:pk>/update/', update_ai_question, name='update-ai-question'),
    path('ai_questions/<int:pk>/delete/', delete_ai_question, name='delete-ai-question'),

    path('ai_answers/', ai_answer_list, name='ai_answer-list'),
    path('ai_answers/<int:pk>/', ai_answer_detail, name='ai_answer-detail'),
    path('ai_answers/create/', create_ai_answer, name='create-ai-answer'),
    path('ai_answers/<int:pk>/update/', update_ai_answer, name='update-ai-answer'),
    path('ai_answers/<int:pk>/delete/', delete_ai_answer, name='delete-ai-answer'),

    path('ai_tool_usages/', ai_tool_usage_list, name='ai_tool_usage-list'),
    path('ai_tool_usages/<int:pk>/', ai_tool_usage_detail, name='ai_tool_usage-detail'),
    path('ai_tool_usages/create/', create_ai_tool_usage, name='create-ai-tool-usage'),
    path('ai_tool_usages/<int:pk>/update/', update_ai_tool_usage, name='update-ai-tool-usage'),
    path('ai_tool_usages/<int:pk>/delete/', delete_ai_tool_usage, name='delete-ai-tool-usage'),
]
