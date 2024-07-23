from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AI_tools.api.views import (
    ConversationViewSet, AIToolViewSet, AIQuestionViewSet, 
    AIAnswerViewSet, AIToolUsageViewSet
)

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'aitools', AIToolViewSet)
router.register(r'aiquestions', AIQuestionViewSet)
router.register(r'aianswers', AIAnswerViewSet)
router.register(r'aitoolusages', AIToolUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
