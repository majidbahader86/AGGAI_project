from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, FooViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'foos', FooViewSet)

urlpatterns = [
    path('', include(router.urls)),
]