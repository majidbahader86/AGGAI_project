# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # DiseaseIdentificationRequest URLs
    path('disease-identification/requests/', views.disease_identification_request_list, name='disease_identification_request_list'),
    path('disease-identification/request/<int:pk>/', views.disease_identification_request_detail, name='disease_identification_request_detail'),

    # ForumPost URLs
    path('forum/posts/', views.forum_post_list, name='forum_post_list'),
    path('forum/post/<int:pk>/', views.forum_post_detail, name='forum_post_detail'),

    # ForumComment URLs
    path('forum/post/<int:post_id>/comments/', views.forum_comment_list, name='forum_comment_list'),
    path('forum/post/<int:post_id>/comment/<int:comment_id>/', views.forum_comment_detail, name='forum_comment_detail'),

    # SeasonAlert URLs
    path('season-alerts/', views.season_alert_list, name='season_alert_list'),
    path('season-alert/<int:pk>/', views.season_alert_detail, name='season_alert_detail'),

    # Authentication URLs
    path('accounts/signup/', views.farmer_sign_up, name='farmer_sign_up'),
    path('accounts/login/', views.farmer_log_in, name='farmer_log_in'),
]
