from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, AIToolViewSet, AIQuestionViewSet, AIAnswerViewSet, AIToolUsageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'ai-tools', AIToolViewSet)
router.register(r'ai-questions', AIQuestionViewSet)
router.register(r'ai-answers', AIAnswerViewSet)
router.register(r'ai-tool-usage', AIToolUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
