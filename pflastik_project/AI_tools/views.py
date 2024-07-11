from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AIToolForm, AIQuestionForm, AIAnswerForm, AIModelForm, AIResultForm
from .models import AITool, AIQuestion, AIAnswer, AIModel, AIResult

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
def ai_tool_list(request):
    tools = AITool.objects.all()
    return render(request, 'ai_tool_list.html', {'tools': tools})

# AI Question Views
@login_required
def create_ai_question(request):
    if request.method == 'POST':
        form = AIQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ai_question_list')
    else:
        form = AIQuestionForm()
    return render(request, 'create_ai_question.html', {'form': form})

@login_required
def ai_question_list(request):
    questions = AIQuestion.objects.all()
    return render(request, 'ai_question_list.html', {'questions': questions})

# AI Answer Views
@login_required
def create_ai_answer(request):
    if request.method == 'POST':
        form = AIAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ai_answer_list')
    else:
        form = AIAnswerForm()
    return render(request, 'create_ai_answer.html', {'form': form})

@login_required
def ai_answer_list(request):
    answers = AIAnswer.objects.all()
    return render(request, 'ai_answer_list.html', {'answers': answers})

# AI Model Views
@login_required
def create_ai_model(request):
    if request.method == 'POST':
        form = AIModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ai_model_list')
    else:
        form = AIModelForm()
    return render(request, 'create_ai_model.html', {'form': form})

@login_required
def ai_model_list(request):
    models = AIModel.objects.all()
    return render(request, 'ai_model_list.html', {'models': models})

# AI Result Views
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

@login_required
def ai_result_list(request):
    results = AIResult.objects.all()
    return render(request, 'ai_result_list.html', {'results': results})
