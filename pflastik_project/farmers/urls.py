from django.urls import path
from . import views

urlpatterns = [
    # Farmer Signup and Login
    path('signup/', views.farmer_signup_view, name='farmer_signup'),
    path('login/', views.farmer_login_view, name='farmer_login'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Monitoring Data
    path('monitoring/data/create/', views.create_monitoring_data, name='create_monitoring_data'),
    path('monitoring/data/list/', views.monitoring_data_list_view, name='monitoring_data_list'),

    # Monitoring Alert
    path('monitoring/alert/create/', views.create_monitoring_alert, name='create_monitoring_alert'),
    path('monitoring/alert/list/', views.monitoring_alert_list_view, name='monitoring_alert_list'),

    # Monitoring Action
    path('monitoring/action/create/', views.create_monitoring_action, name='create_monitoring_action'),
    path('monitoring/action/list/', views.monitoring_action_list_view, name='monitoring_action_list'),

    # Forum
    path('forum/post/create/', views.create_forum_post, name='create_forum_post'),
    path('forum/post/list/', views.forum_post_list_view, name='forum_post_list'),
    path('forum/post/<int:post_id>/', views.forum_post_detail_view, name='forum_post_detail'),
    path('forum/post/<int:post_id>/comment/', views.create_forum_comment, name='create_forum_comment'),

    # Seasonal Alert
    path('season/alert/create/', views.create_season_alert, name='create_season_alert'),
    path('season/alert/list/', views.season_alert_list_view, name='season_alert_list'),

    # Environmental Condition
    path('environmental/condition/create/', views.create_environmental_condition, name='create_environmental_condition'),
    path('environmental/condition/list/', views.environmental_condition_list_view, name='environmental_condition_list'),

    # Care Tip
    path('care/tip/create/', views.create_care_tip, name='create_care_tip'),
    path('care/tip/list/', views.care_tip_list_view, name='care_tip_list'),

    # Financial Aid
    path('financial/aid/create/', views.create_financial_aid, name='create_financial_aid'),
    path('financial/aid/list/', views.financial_aid_list_view, name='financial_aid_list'),
]
