from django.urls import path
from .views import scientist_sign_up, scientist_log_in

urlpatterns = [
    path('signup/', scientist_sign_up, name='scientist_sign_up'),
    path('login/', scientist_log_in, name='scientist_log_in'),
]
