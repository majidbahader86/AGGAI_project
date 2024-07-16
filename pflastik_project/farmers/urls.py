# main_project/urls.py

from django.urls import path, include
from farmers import views as farmers_views  # Import non-API views from farmers app

urlpatterns = [
    # Farmer Signup and Login
    path('signup/', farmers_views.farmer_signup_view, name='farmer_signup'),
    path('login/', farmers_views.farmer_login_view, name='farmer_login'),

    # Dashboard
    path('dashboard/', farmers_views.dashboard_view, name='dashboard'),

    # Monitoring Data
    path('monitoring/data/create/', farmers_views.create_monitoring_data, name='create_monitoring_data'),
    path('monitoring/data/list/', farmers_views.monitoring_data_list_view, name='monitoring_data_list'),

    # Monitoring Alert
    path('monitoring/alert/create/', farmers_views.create_monitoring_alert, name='create_monitoring_alert'),
    path('monitoring/alert/list/', farmers_views.monitoring_alert_list_view, name='monitoring_alert_list'),

    # Monitoring Action
    path('monitoring/action/create/', farmers_views.create_monitoring_action, name='create_monitoring_action'),
    path('monitoring/action/list/', farmers_views.monitoring_action_list_view, name='monitoring_action_list'),

    # Forum
    path('forum/post/create/', farmers_views.create_forum_post, name='create_forum_post'),
    path('forum/post/list/', farmers_views.forum_post_list_view, name='forum_post_list'),
    path('forum/post/<int:post_id>/', farmers_views.forum_post_detail_view, name='forum_post_detail'),
    path('forum/post/<int:post_id>/comment/', farmers_views.create_forum_comment, name='create_forum_comment'),

    # Seasonal Alert
    path('season/alert/create/', farmers_views.create_season_alert, name='create_season_alert'),
    path('season/alert/list/', farmers_views.season_alert_list_view, name='season_alert_list'),

    # Environmental Condition
    path('environmental/condition/create/', farmers_views.create_environmental_condition, name='create_environmental_condition'),
    path('environmental/condition/list/', farmers_views.environmental_condition_list_view, name='environmental_condition_list'),

    # Care Tip
    path('care/tip/create/', farmers_views.create_care_tip, name='create_care_tip'),
    path('care/tip/list/', farmers_views.care_tip_list_view, name='care_tip_list'),

    # Financial Aid
    path('financial/aid/create/', farmers_views.create_financial_aid, name='create_financial_aid'),
    path('financial/aid/list/', farmers_views.financial_aid_list_view, name='financial_aid_list'),

    # Include API URLs
    path('api/farmers/', include('farmers.api.urls')),  # Include the API URLs
]
