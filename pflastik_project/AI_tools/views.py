# views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AITool, AIQuestion, AIAnswer, AIToolUsage

# AITool views
def ai_tool_list(request):
    ai_tools = AITool.objects.all()
    return render(request, 'ai_tool_list.html', {'ai_tools': ai_tools})

def ai_tool_detail(request, pk):
    ai_tool = get_object_or_404(AITool, pk=pk)
    return render(request, 'ai_tool_detail.html', {'ai_tool': ai_tool})

# AIQuestion views
@login_required
def ai_question_list(request):
    questions = AIQuestion.objects.filter(user=request.user)
    return render(request, 'ai_question_list.html', {'questions': questions})

@login_required
def ai_question_detail(request, pk):
    question = get_object_or_404(AIQuestion, pk=pk)
    return render(request, 'ai_question_detail.html', {'question': question})

# AIAnswer views
@login_required
def ai_answer_detail(request, question_id):
    answer = get_object_or_404(AIAnswer, question_id=question_id)
    return render(request, 'ai_answer_detail.html', {'answer': answer})

# AIToolUsage views
@login_required
def ai_tool_usage_list(request):
    tool_usages = AIToolUsage.objects.filter(user=request.user)
    return render(request, 'ai_tool_usage_list.html', {'tool_usages': tool_usages})

@login_required
def ai_tool_usage_detail(request, pk):
    tool_usage = get_object_or_404(AIToolUsage, pk=pk)
    return render(request, 'ai_tool_usage_detail.html', {'tool_usage': tool_usage})
