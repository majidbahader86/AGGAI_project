# account/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ProfileForm, FooForm
from .models import Profile, Foo
from django.contrib.auth.models import User

def index(request):
    # Example index view
    return render(request, 'index.html', {})

def profile_view(request):
    # Example profile view
    # Assuming you have logic to retrieve and display user profile
    return render(request, 'profile.html', {})

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile_detail', user_id=user.id)
    else:
        user_form = UserForm(instance=user)
    return render(request, 'update_user.html', {'user_form': user_form})

def update_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_detail', user_id=profile.user.id)
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'profile_form': profile_form})

def update_foo(request, foo_id=None):
    if foo_id:
        foo = get_object_or_404(Foo, pk=foo_id)
    else:
        foo = None

    if request.method == 'POST':
        foo_form = FooForm(request.POST, instance=foo)
        if foo_form.is_valid():
            foo_form.save()
            return redirect('foo_list')
    else:
        foo_form = FooForm(instance=foo)
    return render(request, 'update_foo.html', {'foo_form': foo_form})