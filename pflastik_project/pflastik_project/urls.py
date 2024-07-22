"""
URL configuration for pflastik_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
def home(request):
    html = """
    <h1>Welcome to Plantastic</h1>
    <ul>
        <li><a href="/admin/">Admin</a></li>
        <li><a href="/accounts/">Accounts</a></li>
        <li><a href="/AI_tools/">AI Tools</a></li>
        <li><a href="/scientists/">Scientists</a></li>
        <li><a href="/plant_disease/">Plant Disease</a></li>
        <li><a href="/farmers/">Farmers</a></li>
    </ul>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  
    path('AI_tools/', include('AI_tools.urls')),  
    path('scientists/', include('scientists.urls')), 
    path('plant_disease/', include('plant_disease.urls')),  
    path('farmers/', include('farmers.urls')),  
]


