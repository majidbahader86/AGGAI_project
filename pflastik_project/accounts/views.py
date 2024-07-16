from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import View, UpdateView
from .forms import UserRegistrationForm, ProfileForm, UserUpdateForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Profile

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile

class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'update_user_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user.username = form
