from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, ProfileForm, UserUpdateForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')  # Redirect to profile after successful registration and login
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')  # Redirect to profile after successful update
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {'profile_form': profile_form})

@login_required
def update_user(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')  # Redirect to profile after successful update
    else:
        user_form = UserUpdateForm(instance=request.user)
    return render(request, 'update_user.html', {'user_form': user_form})

@login_required
def update_user_profile(request):
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('profile')  # Redirect to profile after successful update
    else:
        user_profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'update_user_profile.html', {'user_profile_form': user_profile_form})
