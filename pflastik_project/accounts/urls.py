from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),  # Example traditional view
    path('profile/', views.profile_view, name='profile'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('update_profile/<int:profile_id>/', views.update_profile, name='update_profile'),
    path('update_foo/', views.update_foo, name='update_foo'),
]

