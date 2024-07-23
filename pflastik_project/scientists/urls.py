# scientists/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('publications/new/', views.publication_create, name='publication_create'),
    path('forum/posts/new/', views.forum_post_create, name='forum_post_create'),
    path('forum/posts/<int:post_id>/comments/new/', views.forum_comment_create, name='forum_comment_create'),
    path('experts/new/', views.expert_create, name='expert_create'),
    path('diagnostic-sessions/new/', views.diagnostic_session_create, name='diagnostic_session_create'),
    path('tutorials/new/', views.tutorial_create, name='tutorial_create'),
]
