# forms.py

from django import forms
from .models import AITool, AIQuestion, AIAnswer, AIToolUsage

class AIToolForm(forms.ModelForm):
    class Meta:
        model = AITool
        fields = ['name', 'description', 'model_file', 'usage_instructions']

class AIQuestionForm(forms.ModelForm):
    class Meta:
        model = AIQuestion
        fields = ['question']

class AIAnswerForm(forms.ModelForm):
    class Meta:
        model = AIAnswer
        fields = ['answer']

class AIToolUsageForm(forms.ModelForm):
    class Meta:
        model = AIToolUsage
        fields = ['input_data', 'result']
