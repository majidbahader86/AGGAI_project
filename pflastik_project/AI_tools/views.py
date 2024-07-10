# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AITool, AIQuestion, AIAnswer, AIToolUsage
from .forms import AIToolForm, AIQuestionForm, AIAnswerForm, AIToolUsageForm

# AITool views
def ai_tool_list(request):
    ai_tools = AITool.objects.all()
    return render(request, 'ai_tool_list.html', {'ai_tools': ai_tools})

def ai_tool_detail(request, pk):
    ai_tool = get_object_or_404(AITool, pk=pk)
    return render(request, 'ai_tool_detail.html', {'ai_tool': ai_tool})

@login_required
def ai_tool_create(request):
    if request.method == 'POST':
        form = AIToolForm(request.POST, request.FILES)
        if form.is_valid():
            ai_tool = form.save()
            return redirect('ai_tool_detail', pk=ai_tool.pk)
    else:
        form = AIToolForm()
    return render(request, 'ai_tool_form.html', {'form': form})

@login_required
def ai_tool_update(request, pk):
    ai_tool = get_object_or_404(AITool, pk=pk)
    if request.method == 'POST':
        form = AIToolForm(request.POST, request.FILES, instance=ai_tool)
        if form.is_valid():
            ai_tool = form.save()
            return redirect('ai_tool_detail', pk=ai_tool.pk)
    else:
        form = AIToolForm(instance=ai_tool)
    return render(request, 'ai_tool_form.html', {'form': form, 'ai_tool': ai_tool})

# AIQuestion views
@login_required
def ai_question_list(request):
    questions = AIQuestion.objects.filter(user=request.user)
    return render(request, 'ai_question_list.html', {'questions': questions})

@login_required
def ai_question_detail(request, pk):
    question = get_object_or_404(AIQuestion, pk=pk)
    return render(request, 'ai_question_detail.html', {'question': question})

@login_required
def ai_question_create(request):
    if request.method == 'POST':
        form = AIQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('ai_question_detail', pk=question.pk)
    else:
        form = AIQuestionForm()
    return render(request, 'ai_question_form.html', {'form': form})

# AIAnswer views
@login_required
def ai_answer_detail(request, question_id):
    answer = get_object_or_404(AIAnswer, question_id=question_id)
    return render(request, 'ai_answer_detail.html', {'answer': answer})

@login_required
def ai_answer_create(request, question_id):
    question = get_object_or_404(AIQuestion, pk=question_id)
    if request.method == 'POST':
        form = AIAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('ai_question_detail', pk=question.pk)
    else:
        form = AIAnswerForm()
    return render(request, 'ai_answer_form.html', {'form': form, 'question': question})

# AIToolUsage views
@login_required
def ai_tool_usage_list(request):
    tool_usages = AIToolUsage.objects.filter(user=request.user)
    return render(request, 'ai_tool_usage_list.html', {'tool_usages': tool_usages})

@login_required
def ai_tool_usage_detail(request, pk):
    tool_usage = get_object_or_404(AIToolUsage, pk=pk)
    return render(request, 'ai_tool_usage_detail.html', {'tool_usage': tool_usage})

@login_required
def ai_tool_usage_create(request):
    if request.method == 'POST':
        form = AIToolUsageForm(request.POST)
        if form.is_valid():
            tool_usage = form.save(commit=False)
            tool_usage.user = request.user
            tool_usage.save()
            return redirect('ai_tool_usage_detail', pk=tool_usage.pk)
    else:
        form = AIToolUsageForm()
    return render(request, 'ai_tool_usage_form.html', {'form': form})
