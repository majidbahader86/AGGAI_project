from django.urls import path
from .views import RegisterView, UpdateUserView, UpdateProfileView, UpdateUserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/update_user/', UpdateUserView.as_view(), name='update_user'),
    path('profile/update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/update_user_profile/', UpdateUserProfileView.as_view(), name='update_user_profile'),
]
