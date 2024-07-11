from django.shortcuts import render, redirect
from .models import Publication, AIToolUsage, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial
from .forms import PublicationForm, AIToolUsageForm, ForumPostForm, ForumCommentForm, ExpertForm, DiagnosticSessionForm, TutorialForm

def publication_create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm()
    return render(request, 'publication_form.html', {'form': form})

def aitool_usage_create(request):
    if request.method == 'POST':
        form = AIToolUsageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aitool_usage_list')
    else:
        form = AIToolUsageForm()
    return render(request, 'aitool_usage_form.html', {'form': form})

def forum_post_create(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_post_list')
    else:
        form = ForumPostForm()
    return render(request, 'forum_post_form.html', {'form': form})

def forum_comment_create(request, post_id):
    post = ForumPost.objects.get(id=post_id)
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_post_detail', post_id)
    else:
        form = ForumCommentForm(initial={'post': post})
    return render(request, 'forum_comment_form.html', {'form': form, 'post': post})

def expert_create(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expert_list')
    else:
        form = ExpertForm()
    return render(request, 'expert_form.html', {'form': form})

def diagnostic_session_create(request):
    if request.method == 'POST':
        form = DiagnosticSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnostic_session_list')
    else:
        form = DiagnosticSessionForm()
    return render(request, 'diagnostic_session_form.html', {'form': form})

def tutorial_create(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial_form.html', {'form': form})
