from django.urls import path
from .views import scientist_signup_view, scientist_signin_view

urlpatterns = [
    path('signup/',scientist_signup_view, name='scientist_sign_up'),
    path('login/', scientist_signin_view, name='scientist_log_in'),
]
