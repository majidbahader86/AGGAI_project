from django.urls import path
from . import views

urlpatterns = [
    # Monitoring URLs
    path('monitoring/data/create/', views.create_monitoring_data, name='create_monitoring_data'),
    path('monitoring/alert/create/', views.create_monitoring_alert, name='create_monitoring_alert'),
    path('monitoring/action/create/', views.create_monitoring_action, name='create_monitoring_action'),

    # Forum URLs
    path('forum/post/create/', views.create_forum_post, name='create_forum_post'),
    path('forum/post/<int:post_id>/comment/create/', views.create_forum_comment, name='create_forum_comment'),

    # Seasonal Alerts URLs
    path('season-alert/create/', views.create_season_alert, name='create_season_alert'),

    # Environmental Conditions URLs
    path('environmental-condition/create/', views.create_environmental_condition, name='create_environmental_condition'),

    # Care Tips URLs
    path('care-tip/create/', views.create_care_tip, name='create_care_tip'),

    # European Diseases URLs
    path('european-disease/create/', views.create_european_disease, name='create_european_disease'),

    # Financial Aid URLs
    path('financial-aid/create/', views.create_financial_aid, name='create_financial_aid'),

    # AI Tool URLs
    path('ai-tool/create/', views.create_ai_tool, name='create_ai_tool'),
    path('ai-question/create/', views.create_ai_question, name='create_ai_question'),
    path('ai-question/<int:question_id>/answer/create/', views.create_ai_answer, name='create_ai_answer'),
    path('ai-result/create/', views.create_ai_result, name='create_ai_result'),
]
