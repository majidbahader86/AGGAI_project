from django.urls import path
from . import views

urlpatterns = [
    # Authentication views
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    
    # Monitoring views
    path('monitoring_data/', views.create_monitoring_data, name='create_monitoring_data'),
    path('monitoring_alert/', views.create_monitoring_alert, name='create_monitoring_alert'),
    path('monitoring_action/', views.create_monitoring_action, name='create_monitoring_action'),
    
    # Forum views
    path('forum_post/', views.create_forum_post, name='create_forum_post'),
    path('forum_comment/<int:post_id>/', views.create_forum_comment, name='create_forum_comment'),
    
    # Seasonal Alerts views
    path('season_alert/', views.create_season_alert, name='create_season_alert'),
    
    # Environmental Conditions views
    path('environmental_condition/', views.create_environmental_condition, name='create_environmental_condition'),
    
    # Care Tips views
    path('care_tip/', views.create_care_tip, name='create_care_tip'),
    
    # Financial Aid views
    path('financial_aid/', views.create_financial_aid, name='create_financial_aid'),
]

