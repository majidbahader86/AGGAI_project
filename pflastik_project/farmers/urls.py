from django.urls import path
from .views import farmer_sign_up, farmer_log_in

urlpatterns = [
    path('signup/', farmer_sign_up, name='farmer_sign_up'),
    path('login/', farmer_log_in, name='farmer_log_in'),
]
