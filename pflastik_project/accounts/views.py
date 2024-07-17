from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, FooForm
from .models import Profile, Foo


def index(request):
    context = {
        'welcome_message': 'Welcome to Plantastic!',
        'profiles': Profile.objects.all(),
        'foos': Foo.objects.all(),  
    }
    return render(request, 'index.html', context)
    pass

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_view')
    else:
        profile_form = ProfileForm(instance=profile)
    
    context = {
        'profile': profile,
        'profile_form': profile_form,
    }
    return render(request, 'profile_view.html', context)

# Your views
def update_user(request, user_id):
    user = User.objects.get(pk=user_id)  # Assuming User is imported correctly
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile_detail', user_id=user.id)  # Replace with the appropriate URL name for profile detail view
    else:
        user_form = UserForm(instance=user)
    return render(request, 'update_user.html', {'user_form': user_form})

def update_profile(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_detail', user_id=profile.user.id)  # Replace with the appropriate URL name for profile detail view
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'profile_form': profile_form})

def update_foo(request, foo_id=None):
    if foo_id:
        foo = Foo.objects.get(pk=foo_id)
    else:
        foo = None

    if request.method == 'POST':
        foo_form = FooForm(request.POST, instance=foo)
        if foo_form.is_valid():
            foo_form.save()
            return redirect('foo_list')  # Replace with the appropriate URL name for foo list view
    else:
        foo_form = FooForm(instance=foo)
    return render(request, 'update_foo.html', {'foo_form': foo_form})
