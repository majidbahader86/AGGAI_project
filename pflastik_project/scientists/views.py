from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PublicationForm, ForumPostForm, ForumCommentForm, ExpertForm, DiagnosticSessionForm, TutorialForm, ScientistSignInForm, ScientistSignUpForm
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from .forms import ScientistSignInForm, ScientistSignUpForm
from farmers.models import Plant



@login_required
def publication_create_view(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Replace 'publication_list' with your publication list URL name
    else:
        form = PublicationForm()
    return render(request, 'publication_create.html', {'form': form})

@login_required
def publication_update_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Replace 'publication_list' with your publication list URL name
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'publication_update.html', {'form': form})

@login_required
def publication_delete_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')  # Replace 'publication_list' with your publication list URL name
    return render(request, 'publication_delete.html', {'publication': publication})

@login_required
def forum_post_create_view(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_post_list')  # Replace 'forum_post_list' with your forum post list URL name
    else:
        form = ForumPostForm()
    return render(request, 'forum_post_create.html', {'form': form})

@login_required
def forum_comment_create_view(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('forum_post_detail', post_id=post_id)  # Replace 'forum_post_detail' with your forum post detail URL name
    else:
        form = ForumCommentForm()
    return render(request, 'forum_comment_create.html', {'form': form, 'post': post})

@login_required
def expert_create_view(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expert_list')  # Replace 'expert_list' with your expert list URL name
    else:
        form = ExpertForm()
    return render(request, 'expert_create.html', {'form': form})

@login_required
def diagnostic_session_create_view(request):
    if request.method == 'POST':
        form = DiagnosticSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnostic_session_list')  # Replace 'diagnostic_session_list' with your diagnostic session list URL name
    else:
        form = DiagnosticSessionForm()
    return render(request, 'diagnostic_session_create.html', {'form': form})

@login_required
def tutorial_create_view(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')  # Replace 'tutorial_list' with your tutorial list URL name
    else:
        form = TutorialForm()
    return render(request, 'tutorial_create.html', {'form': form})

def scientist_signin_view(request):
    if request.method == 'POST':
        form = ScientistSignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace 'dashboard' with your scientist dashboard URL name
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = ScientistSignInForm()
    return render(request, 'scientist_signin.html', {'form': form})

def scientist_signup_view(request):
    if request.method == 'POST':
        form = ScientistSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your scientist dashboard URL name
    else:
        form = ScientistSignUpForm()
    return render(request, 'scientist_signup.html', {'form': form})