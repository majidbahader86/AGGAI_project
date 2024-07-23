# scientists/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'publications', views.PublicationViewSet)
router.register(r'forum-posts', views.ForumPostViewSet)
router.register(r'forum-comments', views.ForumCommentViewSet)
router.register(r'experts', views.ExpertViewSet)
router.register(r'diagnostic-sessions', views.DiagnosticSessionViewSet)
router.register(r'tutorials', views.TutorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
