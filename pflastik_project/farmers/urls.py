from django.urls import path
from . import views

urlpatterns = [
    # Farmer Signup and Login URLs
    path('signup/', views.farmer_signup_view, name='farmer_signup'),
    path('login/', views.farmer_login_view, name='farmer_login'),

    # Monitoring URLs
    path('monitoring/data/', views.monitoring_data_view, name='monitoring_data'),
    path('monitoring/data/list/', views.monitoring_data_list_view, name='monitoring_data_list'),
    path('monitoring/action/', views.monitoring_action_view, name='monitoring_action'),
    path('monitoring/action/list/', views.monitoring_action_list_view, name='monitoring_action_list'),

    # Forum URLs
    path('forum/post/', views.forum_post_view, name='forum_post'),
    path('forum/post/list/', views.forum_post_list_view, name='forum_post_list'),
    path('forum/comment/', views.forum_comment_view, name='forum_comment'),
    path('forum/comment/list/', views.forum_comment_list_view, name='forum_comment_list'),

    # Seasonal Alerts URLs
    path('season/alert/', views.season_alert_view, name='season_alert'),
    path('season/alert/list/', views.season_alert_list_view, name='season_alert_list'),

    # Environmental Conditions URLs
    path('environmental/condition/', views.environmental_condition_view, name='environmental_condition'),
    path('environmental/condition/list/', views.environmental_condition_list_view, name='environmental_condition_list'),

    # Care Tips URLs
    path('care/tip/', views.care_tip_view, name='care_tip'),
    path('care/tip/list/', views.care_tip_list_view, name='care_tip_list'),

    # Financial Aid URLs
    path('financial/aid/', views.financial_aid_view, name='financial_aid'),
    path('financial/aid/list/', views.financial_aid_list_view, name='financial_aid_list'),

    # Dashboard URL
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

