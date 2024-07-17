# farmers/api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # MonitoringData URLs
    path('monitoring_data/', views.MonitoringDataListCreateView.as_view(), name='monitoring_data_list_create'),
    path('monitoring_data/<int:pk>/', views.MonitoringDataDetailView.as_view(), name='monitoring_data_detail'),

    # MonitoringAlert URLs
    path('monitoring_alerts/', views.MonitoringAlertListCreateView.as_view(), name='monitoring_alert_list_create'),
    path('monitoring_alerts/<int:pk>/', views.MonitoringAlertDetailView.as_view(), name='monitoring_alert_detail'),

    # MonitoringAction URLs
    path('monitoring_actions/', views.MonitoringActionListCreateView.as_view(), name='monitoring_action_list_create'),
    path('monitoring_actions/<int:pk>/', views.MonitoringActionDetailView.as_view(), name='monitoring_action_detail'),

    # ForumPost URLs
    path('forum_posts/', views.ForumPostListCreateView.as_view(), name='forum_post_list_create'),
    path('forum_posts/<int:pk>/', views.ForumPostDetailView.as_view(), name='forum_post_detail'),

    # ForumComment URLs
    path('forum_comments/', views.ForumCommentListCreateView.as_view(), name='forum_comment_list_create'),
    path('forum_comments/<int:pk>/', views.ForumCommentDetailView.as_view(), name='forum_comment_detail'),

    # SeasonAlert URLs
    path('season_alerts/', views.SeasonAlertListCreateView.as_view(), name='season_alert_list_create'),
    path('season_alerts/<int:pk>/', views.SeasonAlertDetailView.as_view(), name='season_alert_detail'),

    # EnvironmentalCondition URLs
    path('environmental_conditions/', views.EnvironmentalConditionListCreateView.as_view(), name='environmental_condition_list_create'),
    path('environmental_conditions/<int:pk>/', views.EnvironmentalConditionDetailView.as_view(), name='environmental_condition_detail'),

    # CareTip URLs
    path('care_tips/', views.CareTipListCreateView.as_view(), name='care_tip_list_create'),
    path('care_tips/<int:pk>/', views.CareTipDetailView.as_view(), name='care_tip_detail'),

    # FinancialAid URLs
    path('financial_aid/', views.FinancialAidListCreateView.as_view(), name='financial_aid_list_create'),
    path('financial_aid/<int:pk>/', views.FinancialAidDetailView.as_view(), name='financial_aid_detail'),
]