# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import (
    MonitoringDataForm, MonitoringAlertForm, MonitoringActionForm, 
    ForumPostForm, ForumCommentForm, SeasonAlertForm, EnvironmentalConditionForm, 
    CareTipForm, FinancialAidForm, FarmerSignupForm
)
from .models import (
    MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment, 
    SeasonAlert, EnvironmentalCondition, CareTip, FinancialAid, 
)

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

@login_required
def create_monitoring_data(request):
    if request.method == 'POST':
        form = MonitoringDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_data_list')
    else:
        form = MonitoringDataForm()
    return render(request, 'farmers/create_monitoring_data.html', {'form': form})

@login_required
def create_monitoring_alert(request):
    if request.method == 'POST':
        form = MonitoringAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_alert_list')
    else:
        form = MonitoringAlertForm()
    return render(request, 'farmers/create_monitoring_alert.html', {'form': form})

@login_required
def create_monitoring_action(request):
    if request.method == 'POST':
        form = MonitoringActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_action_list')
    else:
        form = MonitoringActionForm()
    return render(request, 'farmers/create_monitoring_action.html', {'form': form})

# Forum Views

@login_required
def create_forum_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('forum_post_list')
    else:
        form = ForumPostForm()
    return render(request, 'farmers/create_forum_post.html', {'form': form})

@login_required
def create_forum_comment(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('forum_post_detail', post_id=post.id)
    else:
        form = ForumCommentForm()
    return render(request, 'farmers/create_forum_comment.html', {'form': form, 'post': post})

# Seasonal Alerts Views

@login_required
def create_season_alert(request):
    if request.method == 'POST':
        form = SeasonAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_alert_list')
    else:
        form = SeasonAlertForm()
    return render(request, 'farmers/create_season_alert.html', {'form': form})

# Environmental Conditions Views

@login_required
def create_environmental_condition(request):
    if request.method == 'POST':
        form = EnvironmentalConditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('environmental_condition_list')
    else:
        form = EnvironmentalConditionForm()
    return render(request, 'farmers/create_environmental_condition.html', {'form': form})

# Care Tips Views

@login_required
def create_care_tip(request):
    if request.method == 'POST':
        form = CareTipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('care_tip_list')
    else:
        form = CareTipForm()
    return render(request, 'farmers/create_care_tip.html', {'form': form})

# Financial Aid Views

@login_required
def create_financial_aid(request):
    if request.method == 'POST':
        form = FinancialAidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financial_aid_list')
    else:
        form = FinancialAidForm()
    return render(request, 'farmers/create_financial_aid.html', {'form': form})

# Dashboard View

@login_required
def dashboard_view(request):
    # Example view for dashboard after login
    return render(request, 'farmers/dashboard.html')
