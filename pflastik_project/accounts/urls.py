from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example traditional view
    path('profile/', views.profile_view, name='profile'),
    path('update/user/<int:user_id>/', views.update_user, name='update_user'),
    path('update/profile/<int:profile_id>/', views.update_profile, name='update_profile'),
    path('update/foo/<int:foo_id>/', views.update_foo, name='update_foo'),
   
]