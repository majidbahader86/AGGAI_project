from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import (
    SignUpForm, SignInForm, PublicationForm, ForumPostForm, ForumCommentForm, 
    ExpertForm, DiagnosticSessionForm, TutorialForm
)
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from .serializers import (
    PublicationSerializer, ForumPostSerializer, ForumCommentSerializer, 
    ExpertSerializer, DiagnosticSessionSerializer, TutorialSerializer
)

# Django views for handling forms
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

def publication_create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Redirect to a success page or list page
    else:
        form = PublicationForm()
    return render(request, 'publication_form.html', {'form': form})

def forum_post_create(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_post_list')  # Redirect to a success page or list page
    else:
        form = ForumPostForm()
    return render(request, 'forum_post_form.html', {'form': form})

def forum_comment_create(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('forum_post_detail', post_id=post_id)  # Redirect to post detail page
    else:
        form = ForumCommentForm()
    return render(request, 'forum_comment_form.html', {'form': form})

def expert_create(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expert_list')  # Redirect to a success page or list page
    else:
        form = ExpertForm()
    return render(request, 'expert_form.html', {'form': form})

def diagnostic_session_create(request):
    if request.method == 'POST':
        form = DiagnosticSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnostic_session_list')  # Redirect to a success page or list page
    else:
        form = DiagnosticSessionForm()
    return render(request, 'diagnostic_session_form.html', {'form': form})

def tutorial_create(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')  # Redirect to a success page or list page
    else:
        form = TutorialForm()
    return render(request, 'tutorial_form.html', {'form': form})
