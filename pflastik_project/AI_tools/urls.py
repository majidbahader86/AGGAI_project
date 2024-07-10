# urls.py

from django.urls import path
from . import views

app_name = 'ai_tools'

urlpatterns = [
    # AITool URLs
    path('ai_tools/', views.ai_tool_list, name='ai_tool_list'),
    path('ai_tools/<int:pk>/', views.ai_tool_detail, name='ai_tool_detail'),
    path('ai_tools/create/', views.ai_tool_create, name='ai_tool_create'),
    path('ai_tools/<int:pk>/update/', views.ai_tool_update, name='ai_tool_update'),

    # AIQuestion URLs
    path('ai_questions/', views.ai_question_list, name='ai_question_list'),
    path('ai_questions/<int:pk>/', views.ai_question_detail, name='ai_question_detail'),
    path('ai_questions/create/', views.ai_question_create, name='ai_question_create'),

    # AIAnswer URLs
    path('ai_questions/<int:question_id>/answer/', views.ai_answer_create, name='ai_answer_create'),

    # AIToolUsage URLs
    path('ai_tool_usage/', views.ai_tool_usage_list, name='ai_tool_usage_list'),
    path('ai_tool_usage/<int:pk>/', views.ai_tool_usage_detail, name='ai_tool_usage_detail'),
    path('ai_tool_usage/create/', views.ai_tool_usage_create, name='ai_tool_usage_create'),
]
