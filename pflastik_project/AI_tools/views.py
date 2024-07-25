from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage
from .api.serializers import ConversationSerializer, AIToolSerializer, AIQuestionSerializer, AIAnswerSerializer, AIToolUsageSerializer

# For Conversations
@require_http_methods(["GET"])
def conversation_list(request):
    conversations = Conversation.objects.all()
    return JsonResponse({'conversations': list(conversations.values())})

@require_http_methods(["GET"])
def conversation_detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    return JsonResponse({
        'id': conversation.id,
        'user': conversation.user.username,
        'llm_name': conversation.llm_name,
        'timestamp': conversation.timestamp,
        'user_messages': conversation.user_messages,
        'llm_responses': conversation.llm_responses,
        'context': conversation.context
    })

@csrf_exempt
@require_http_methods(["POST"])
def create_conversation(request):
    import json
    data = json.loads(request.body)
    conversation = Conversation.objects.create(
        user=User.objects.get(id=data['user']),
        llm_name=data['llm_name'],
        user_messages=data['user_messages'],
        llm_responses=data['llm_responses'],
        context=data.get('context', {})
    )
    return JsonResponse({'id': conversation.id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_conversation(request, pk):
    import json
    data = json.loads(request.body)
    conversation = get_object_or_404(Conversation, pk=pk)
    conversation.llm_name = data.get('llm_name', conversation.llm_name)
    conversation.user_messages = data.get('user_messages', conversation.user_messages)
    conversation.llm_responses = data.get('llm_responses', conversation.llm_responses)
    conversation.context = data.get('context', conversation.context)
    conversation.save()
    return JsonResponse({'status': 'updated'})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_conversation(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    conversation.delete()
    return JsonResponse({'status': 'deleted'})

# For AITool
@require_http_methods(["GET"])
def ai_tool_list(request):
    ai_tools = AITool.objects.all()
    return JsonResponse({'ai_tools': list(ai_tools.values())})

@require_http_methods(["GET"])
def ai_tool_detail(request, pk):
    ai_tool = get_object_or_404(AITool, pk=pk)
    return JsonResponse({
        'id': ai_tool.id,
        'name': ai_tool.name,
        'description': ai_tool.description,
        'model_file': ai_tool.model_file.url,
        'usage_instructions': ai_tool.usage_instructions
    })

@csrf_exempt
@require_http_methods(["POST"])
def create_ai_tool(request):
    import json
    data = json.loads(request.body)
    ai_tool = AITool.objects.create(
        name=data['name'],
        description=data['description'],
        model_file=data['model_file'],
        usage_instructions=data['usage_instructions']
    )
    return JsonResponse({'id': ai_tool.id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_ai_tool(request, pk):
    import json
    data = json.loads(request.body)
    ai_tool = get_object_or_404(AITool, pk=pk)
    ai_tool.name = data.get('name', ai_tool.name)
    ai_tool.description = data.get('description', ai_tool.description)
    ai_tool.model_file = data.get('model_file', ai_tool.model_file)
    ai_tool.usage_instructions = data.get('usage_instructions', ai_tool.usage_instructions)
    ai_tool.save()
    return JsonResponse({'status': 'updated'})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_ai_tool(request, pk):
    ai_tool = get_object_or_404(AITool, pk=pk)
    ai_tool.delete()
    return JsonResponse({'status': 'deleted'})

# For AIQuestion
@require_http_methods(["GET"])
def ai_question_list(request):
    ai_questions = AIQuestion.objects.all()
    return JsonResponse({'ai_questions': list(ai_questions.values())})

@require_http_methods(["GET"])
def ai_question_detail(request, pk):
    ai_question = get_object_or_404(AIQuestion, pk=pk)
    return JsonResponse({
        'id': ai_question.id,
        'user': ai_question.user.username,
        'question': ai_question.question,
        'created_at': ai_question.created_at
    })

@csrf_exempt
@require_http_methods(["POST"])
def create_ai_question(request):
    import json
    data = json.loads(request.body)
    ai_question = AIQuestion.objects.create(
        user=User.objects.get(id=data['user']),
        question=data['question']
    )
    return JsonResponse({'id': ai_question.id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_ai_question(request, pk):
    import json
    data = json.loads(request.body)
    ai_question = get_object_or_404(AIQuestion, pk=pk)
    ai_question.question = data.get('question', ai_question.question)
    ai_question.save()
    return JsonResponse({'status': 'updated'})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_ai_question(request, pk):
    ai_question = get_object_or_404(AIQuestion, pk=pk)
    ai_question.delete()
    return JsonResponse({'status': 'deleted'})

# For AIAnswer
@require_http_methods(["GET"])
def ai_answer_list(request):
    ai_answers = AIAnswer.objects.all()
    return JsonResponse({'ai_answers': list(ai_answers.values())})

@require_http_methods(["GET"])
def ai_answer_detail(request, pk):
    ai_answer = get_object_or_404(AIAnswer, pk=pk)
    return JsonResponse({
        'id': ai_answer.id,
        'question': ai_answer.question.question,
        'answer': ai_answer.answer
    })

@csrf_exempt
@require_http_methods(["POST"])
def create_ai_answer(request):
    import json
    data = json.loads(request.body)
    ai_answer = AIAnswer.objects.create(
        question=AIQuestion.objects.get(id=data['question']),
        answer=data['answer']
    )
    return JsonResponse({'id': ai_answer.id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_ai_answer(request, pk):
    import json
    data = json.loads(request.body)
    ai_answer = get_object_or_404(AIAnswer, pk=pk)
    ai_answer.answer = data.get('answer', ai_answer.answer)
    ai_answer.save()
    return JsonResponse({'status': 'updated'})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_ai_answer(request, pk):
    ai_answer = get_object_or_404(AIAnswer, pk=pk)
    ai_answer.delete()
    return JsonResponse({'status': 'deleted'})

# For AIToolUsage
@require_http_methods(["GET"])
def ai_tool_usage_list(request):
    ai_tool_usages = AIToolUsage.objects.all()
    return JsonResponse({'ai_tool_usages': list(ai_tool_usages.values())})

@require_http_methods(["GET"])
def ai_tool_usage_detail(request, pk):
    ai_tool_usage = get_object_or_404(AIToolUsage, pk=pk)
    return JsonResponse({
        'id': ai_tool_usage.id,
        'tool': ai_tool_usage.tool.name,
        'user': ai_tool_usage.user.username,
        'input_data': ai_tool_usage.input_data,
        'result': ai_tool_usage.result,
        'usage_date': ai_tool_usage.usage_date
    })

@csrf_exempt
@require_http_methods(["POST"])
def create_ai_tool_usage(request):
    import json
    data = json.loads(request.body)
    ai_tool_usage = AIToolUsage.objects.create(
        tool=AITool.objects.get(id=data['tool']),
        user=User.objects.get(id=data['user']),
        input_data=data['input_data'],
        result=data['result']
    )
    return JsonResponse({'id': ai_tool_usage.id}, status=201)

@csrf_exempt
@require_http_methods(["PUT"])
def update_ai_tool_usage(request, pk):
    import json
    data = json.loads(request.body)
    ai_tool_usage = get_object_or_404(AIToolUsage, pk=pk)
    ai_tool_usage.input_data = data.get('input_data', ai_tool_usage.input_data)
    ai_tool_usage.result = data.get('result', ai_tool_usage.result)
    ai_tool_usage.save()
    return JsonResponse({'status': 'updated'})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_ai_tool_usage(request, pk):
    ai_tool_usage = get_object_or_404(AIToolUsage, pk=pk)
    ai_tool_usage.delete()
    return JsonResponse({'status': 'deleted'})
