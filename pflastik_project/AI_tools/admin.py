from django.contrib import admin

from django.contrib import admin
from .models import AITool, AIQuestion, AIAnswer, AIToolUsage, Conversation

# Register your models here
@admin.register(AITool)
class AIToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(AIQuestion)
class AIQuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'question')

@admin.register(AIAnswer)
class AIAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question__question',)

@admin.register(AIToolUsage)
class AIToolUsageAdmin(admin.ModelAdmin):
    list_display = ('tool', 'user', 'usage_date')
    list_filter = ('usage_date',)
    search_fields = ('tool__name', 'user__username')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'llm_name', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'llm_name')


