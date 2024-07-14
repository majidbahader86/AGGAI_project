from django.urls import path
from . import views

urlpatterns = [
    # Publications
    path('publications/', views.publication_list_view, name='publication_list'),
    path('publications/create/', views.publication_create_view, name='publication_create'),
    path('publications/<int:pk>/update/', views.publication_update_view, name='publication_update'),
    path('publications/<int:pk>/delete/', views.publication_delete_view, name='publication_delete'),

    # Forum Posts
    path('forum/posts/', views.forum_post_list_view, name='forum_post_list'),
    path('forum/posts/create/', views.forum_post_create_view, name='forum_post_create'),

    # Forum Comments (assuming comments are created within the post detail view)
    path('forum/posts/<int:post_id>/comments/create/', views.forum_comment_create_view, name='forum_comment_create'),

    # Experts
    path('experts/', views.expert_list_view, name='expert_list'),
    path('experts/create/', views.expert_create_view, name='expert_create'),

    # Diagnostic Sessions
    path('diagnostics/sessions/', views.diagnostic_session_list_view, name='diagnostic_session_list'),
    path('diagnostics/sessions/create/', views.diagnostic_session_create_view, name='diagnostic_session_create'),

    # Tutorials
    path('tutorials/', views.tutorial_list_view, name='tutorial_list'),
    path('tutorials/create/', views.tutorial_create_view, name='tutorial_create'),

    # Scientist Sign-in and Sign-up
    path('scientist/signin/', views.scientist_signin_view, name='scientist_signin'),
    path('scientist/signup/', views.scientist_signup_view, name='scientist_signup'),
]
