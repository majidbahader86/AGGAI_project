# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import MonitoringDataForm, MonitoringActionForm, ForumPostForm, ForumCommentForm, \
    SeasonAlertForm, EnvironmentalConditionForm, CareTipForm, FinancialAidForm, FarmerSignupForm
from .models import Profile, MonitoringData, MonitoringAction, ForumPost, ForumComment, \
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid
from disease_detection.models import DiseaseIdentificationRequest
from django.contrib.auth.models import User


# Farmer Signup and Login Views

def farmer_signup_view(request):
    if request.method == 'POST':
        form = FarmerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('dashboard')  # Redirect to dashboard or any other URL
    else:
        form = FarmerSignupForm()
    return render(request, 'farmers/farmer_signup.html', {'form': form})

def farmer_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.profile.is_farmer:  # Assuming profile.is_farmer is True for farmers
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or any other URL
    else:
        form = AuthenticationForm()
    return render(request, 'farmers/farmer_login.html', {'form': form})

# Monitoring Views

def monitoring_data_view(request):
    if request.method == 'POST':
        form = MonitoringDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_data_list')  # Redirect to list view of monitoring data
    else:
        form = MonitoringDataForm()
    return render(request, 'farmers/monitoring_data_form.html', {'form': form})

def monitoring_data_list_view(request):
    monitoring_data = MonitoringData.objects.all()
    return render(request, 'farmers/monitoring_data_list.html', {'monitoring_data': monitoring_data})

def monitoring_action_view(request):
    if request.method == 'POST':
        form = MonitoringActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_action_list')  # Redirect to list view of monitoring actions
    else:
        form = MonitoringActionForm()
    return render(request, 'farmers/monitoring_action_form.html', {'form': form})

def monitoring_action_list_view(request):
    monitoring_actions = MonitoringAction.objects.all()
    return render(request, 'farmers/monitoring_action_list.html', {'monitoring_actions': monitoring_actions})

# Forum Views

def forum_post_view(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_post_list')  # Redirect to list view of forum posts
    else:
        form = ForumPostForm()
    return render(request, 'farmers/forum_post_form.html', {'form': form})

def forum_post_list_view(request):
    forum_posts = ForumPost.objects.all()
    return render(request, 'farmers/forum_post_list.html', {'forum_posts': forum_posts})

def forum_comment_view(request):
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_comment_list')  # Redirect to list view of forum comments
    else:
        form = ForumCommentForm()
    return render(request, 'farmers/forum_comment_form.html', {'form': form})

def forum_comment_list_view(request):
    forum_comments = ForumComment.objects.all()
    return render(request, 'farmers/forum_comment_list.html', {'forum_comments': forum_comments})

# Seasonal Alerts Views

def season_alert_view(request):
    if request.method == 'POST':
        form = SeasonAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_alert_list')  # Redirect to list view of seasonal alerts
    else:
        form = SeasonAlertForm()
    return render(request, 'farmers/season_alert_form.html', {'form': form})

def season_alert_list_view(request):
    season_alerts = SeasonAlert.objects.all()
    return render(request, 'farmers/season_alert_list.html', {'season_alerts': season_alerts})

# Environmental Conditions Views

def environmental_condition_view(request):
    if request.method == 'POST':
        form = EnvironmentalConditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('environmental_condition_list')  # Redirect to list view of environmental conditions
    else:
        form = EnvironmentalConditionForm()
    return render(request, 'farmers/environmental_condition_form.html', {'form': form})

def environmental_condition_list_view(request):
    environmental_conditions = EnvironmentalCondition.objects.all()
    return render(request, 'farmers/environmental_condition_list.html', {'environmental_conditions': environmental_conditions})

# Care Tips Views

def care_tip_view(request):
    if request.method == 'POST':
        form = CareTipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('care_tip_list')  # Redirect to list view of care tips
    else:
        form = CareTipForm()
    return render(request, 'farmers/care_tip_form.html', {'form': form})

def care_tip_list_view(request):
    care_tips = CareTip.objects.all()
    return render(request, 'farmers/care_tip_list.html', {'care_tips': care_tips})

# Financial Aid Views

def financial_aid_view(request):
    if request.method == 'POST':
        form = FinancialAidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financial_aid_list')  # Redirect to list view of financial aids
    else:
        form = FinancialAidForm()
    return render(request, 'farmers/financial_aid_form.html', {'form': form})

def financial_aid_list_view(request):
    financial_aids = FinancialAid.objects.all()
    return render(request, 'farmers/financial_aid_list.html', {'financial_aids': financial_aids})

# Dashboard View

def dashboard_view(request):
    # Example view for dashboard after login
    return render(request, 'farmers/dashboard.html')
