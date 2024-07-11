from django.urls import path
from . import views

urlpatterns = [
    path('ai-tools/create/', views.create_ai_tool, name='create_ai_tool'),
    path('ai-tools/', views.ai_tool_list, name='ai_tool_list'),
    
    path('ai-questions/create/', views.create_ai_question, name='create_ai_question'),
    path('ai-questions/', views.ai_question_list, name='ai_question_list'),
    
    path('ai-answers/create/', views.create_ai_answer, name='create_ai_answer'),
    path('ai-answers/', views.ai_answer_list, name='ai_answer_list'),
    
    path('ai-models/create/', views.create_ai_model, name='create_ai_model'),
    path('ai-models/', views.ai_model_list, name='ai_model_list'),
    
    path('ai-results/create/', views.create_ai_result, name='create_ai_result'),
    path('ai-results/', views.ai_result_list, name='ai_result_list'),
]
