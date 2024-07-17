from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiseaseIdentificationRequestViewSet

router = DefaultRouter()
router.register(r'disease-identification-requests', DiseaseIdentificationRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]