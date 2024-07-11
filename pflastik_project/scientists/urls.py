from django.urls import path
from . import views

urlpatterns = [
    path('publication/create/', views.publication_create, name='publication_create'),
    path('aitool/usage/create/', views.aitool_usage_create, name='aitool_usage_create'),
    path('forum/post/create/', views.forum_post_create, name='forum_post_create'),
    path('forum/post/<int:post_id>/comment/create/', views.forum_comment_create, name='forum_comment_create'),
    path('expert/create/', views.expert_create, name='expert_create'),
    path('diagnostic/session/create/', views.diagnostic_session_create, name='diagnostic_session_create'),
    path('tutorial/create/', views.tutorial_create, name='tutorial_create'),
]
