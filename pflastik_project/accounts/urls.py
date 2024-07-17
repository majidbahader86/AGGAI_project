from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example traditional view
    path('profile/', views.profile_view, name='profile'),
    path('api/', include('account.api.urls')),  # Include API URLs
]
