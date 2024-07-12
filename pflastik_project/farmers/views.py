from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import (
    
    MonitoringDataForm, MonitoringAlertForm, MonitoringActionForm, 
    ForumPostForm, ForumCommentForm, SeasonAlertForm, EnvironmentalConditionForm, 
    CareTipForm, EuropeanDiseaseForm, FinancialAidForm, AIToolForm, AIQuestionForm, 
    AIAnswerForm, AIResultForm
)
from .models import (
    MonitoringData, MonitoringAlert, MonitoringAction, ForumPost, ForumComment, 
    SeasonAlert, EnvironmentalCondition, CareTip, EuropeanDisease, FinancialAid, 
    AITool, AIQuestion, AIAnswer, AIResult
)

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
    return render(request, 'create_monitoring_data.html', {'form': form})

@login_required
def create_monitoring_alert(request):
    if request.method == 'POST':
        form = MonitoringAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_alert_list')
    else:
        form = MonitoringAlertForm()
    return render(request, 'create_monitoring_alert.html', {'form': form})

@login_required
def create_monitoring_action(request):
    if request.method == 'POST':
        form = MonitoringActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_action_list')
    else:
        form = MonitoringActionForm()
    return render(request, 'create_monitoring_action.html', {'form': form})

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
    return render(request, 'create_forum_post.html', {'form': form})

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
    return render(request, 'create_forum_comment.html', {'form': form, 'post': post})

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
    return render(request, 'create_season_alert.html', {'form': form})

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
    return render(request, 'create_environmental_condition.html', {'form': form})

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
    return render(request, 'create_care_tip.html', {'form': form})

# European Diseases Views
@login_required
def create_european_disease(request):
    if request.method == 'POST':
        form = EuropeanDiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('european_disease_list')
    else:
        form = EuropeanDiseaseForm()
    return render(request, 'create_european_disease.html', {'form': form})

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
    return render(request, 'create_financial_aid.html', {'form': form})

# AI Tool Views
@login_required
def create_ai_tool(request):
    if request.method == 'POST':
        form = AIToolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ai_tool_list')
    else:
        form = AIToolForm()
    return render(request, 'create_ai_tool.html', {'form': form})

@login_required
def create_ai_question(request):
    if request.method == 'POST':
        form = AIQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('ai_question_list')
    else:
        form = AIQuestionForm()
    return render(request, 'create_ai_question.html', {'form': form})

@login_required
def create_ai_answer(request, question_id):
    question = get_object_or_404(AIQuestion, id=question_id)
    if request.method == 'POST':
        form = AIAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('ai_question_detail', question_id=question.id)
    else:
        form = AIAnswerForm()
    return render(request, 'create_ai_answer.html', {'form': form, 'question': question})

@login_required
def create_ai_result(request):
    if request.method == 'POST':
        form = AIResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ai_result_list')
    else:
        form = AIResultForm()
    return render(request, 'create_ai_result.html', {'form': form})
