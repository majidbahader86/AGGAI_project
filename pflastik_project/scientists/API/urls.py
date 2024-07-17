
# scientists/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('publications/', views.PublicationListCreateAPIView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', views.PublicationRetrieveUpdateDestroyAPIView.as_view(), name='publication-detail'),
    path('forum-posts/', views.ForumPostListCreateAPIView.as_view(), name='forum-post-list'),
    path('forum-posts/<int:pk>/', views.ForumPostRetrieveUpdateDestroyAPIView.as_view(), name='forum-post-detail'),
    path('forum-comments/', views.ForumCommentListCreateAPIView.as_view(), name='forum-comment-list'),
    path('forum-comments/<int:pk>/', views.ForumCommentRetrieveUpdateDestroyAPIView.as_view(), name='forum-comment-detail'),
    path('experts/', views.ExpertListCreateAPIView.as_view(), name='expert-list'),
    path('experts/<int:pk>/', views.ExpertRetrieveUpdateDestroyAPIView.as_view(), name='expert-detail'),
    path('diagnostic-sessions/', views.DiagnosticSessionListCreateAPIView.as_view(), name='diagnostic-session-list'),
    path('diagnostic-sessions/<int:pk>/', views.DiagnosticSessionRetrieveUpdateDestroyAPIView.as_view(), name='diagnostic-session-detail'),
    path('tutorials/', views.TutorialListCreateAPIView.as_view(), name='tutorial-list'),
    path('tutorials/<int:pk>/', views.TutorialRetrieveUpdateDestroyAPIView.as_view(), name='tutorial-detail'),
]
