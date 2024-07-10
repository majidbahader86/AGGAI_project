# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login, login_required, authenticate
from .models import DiseaseIdentificationRequest, ForumPost, ForumComment, SeasonAlert
from .forms import FarmerSignUpForm, FarmerLoginForm

# DiseaseIdentificationRequest views
@login_required
def disease_identification_request_list(request):
    requests = DiseaseIdentificationRequest.objects.filter(user=request.user)
    return render(request, 'disease_identification_request_list.html', {'requests': requests})

@login_required
def disease_identification_request_detail(request, pk):
    request = get_object_or_404(DiseaseIdentificationRequest, pk=pk)
    return render(request, 'disease_identification_request_detail.html', {'request': request})

# ForumPost views
@login_required
def forum_post_list(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum_post_list.html', {'posts': posts})

@login_required
def forum_post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    return render(request, 'forum_post_detail.html', {'post': post})

# ForumComment views
@login_required
def forum_comment_list(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)
    comments = post.comments.all()
    return render(request, 'forum_comment_list.html', {'post': post, 'comments': comments})

@login_required
def forum_comment_detail(request, post_id, comment_id):
    comment = get_object_or_404(ForumComment, pk=comment_id)
    return render(request, 'forum_comment_detail.html', {'comment': comment})

# SeasonAlert views
def season_alert_list(request):
    alerts = SeasonAlert.objects.all()
    return render(request, 'season_alert_list.html', {'alerts': alerts})

def season_alert_detail(request, pk):
    alert = get_object_or_404(SeasonAlert, pk=pk)
    return render(request, 'season_alert_detail.html', {'alert': alert})


def farmer_sign_up(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('farmer_dashboard')  # Redirect to farmer's dashboard
    else:
        form = FarmerSignUpForm()
    return render(request, 'farmers/sign_up.html', {'form': form})

def farmer_log_in(request):
    if request.method == 'POST':
        form = FarmerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('farmer_dashboard')  # Redirect to farmer's dashboard
    else:
        form = FarmerLoginForm()
    return render(request, 'farmers/login.html', {'form': form})