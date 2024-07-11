from django import forms
from .models import AITool, AIQuestion, AIAnswer, AIModel, AIResult

class AIToolForm(forms.ModelForm):
    class Meta:
        model = AITool
        fields = ['name', 'description', 'model_file', 'usage_instructions']

class AIQuestionForm(forms.ModelForm):
    class Meta:
        model = AIQuestion
        fields = ['user', 'question']

class AIAnswerForm(forms.ModelForm):
    class Meta:
        model = AIAnswer
        fields = ['question', 'answer']

class AIModelForm(forms.ModelForm):
    class Meta:
        model = AIModel
        fields = ['name', 'description', 'model_file']

class AIResultForm(forms.ModelForm):
    class Meta:
        model = AIResult
        fields = ['model', 'result_data']
