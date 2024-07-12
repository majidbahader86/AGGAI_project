from django import forms
from django.contrib.auth.models import User
from .models import (
    MonitoringData, MonitoringAlert, MonitoringAction, 
    ForumPost, ForumComment, SeasonAlert, EnvironmentalCondition, 
    CareTip, EuropeanDisease, FinancialAid, AITool, AIQuestion, 
    AIAnswer, AIResult
)

# Form for Monitoring Data
class MonitoringDataForm(forms.ModelForm):
    class Meta:
        model = MonitoringData
        fields = ['temperature', 'humidity', 'soil_moisture']

# Form for Monitoring Alert
class MonitoringAlertForm(forms.ModelForm):
    class Meta:
        model = MonitoringAlert
        fields = ['alert_type', 'alert_message']

# Form for Monitoring Action
class MonitoringActionForm(forms.ModelForm):
    class Meta:
        model = MonitoringAction
        fields = ['name']

# Form for Forum Post
class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']

# Form for Forum Comment
class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['post', 'content']

# Form for Season Alert
class SeasonAlertForm(forms.ModelForm):
    class Meta:
        model = SeasonAlert
        fields = ['crop', 'alert_type', 'alert_message']

# Form for Environmental Condition
class EnvironmentalConditionForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalCondition
        fields = ['temperature', 'humidity', 'soil_moisture', 'alert_message']

# Form for Care Tip
class CareTipForm(forms.ModelForm):
    class Meta:
        model = CareTip
        fields = ['crop', 'region', 'tip']

# Form for European Disease
class EuropeanDiseaseForm(forms.ModelForm):
    class Meta:
        model = EuropeanDisease
        fields = ['name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']
        widgets = {
            'affected_parts': forms.CheckboxSelectMultiple,
        }

# Form for Financial Aid
class FinancialAidForm(forms.ModelForm):
    class Meta:
        model = FinancialAid
        fields = ['crop', 'price', 'transaction_date']

# Form for AI Tool
class AIToolForm(forms.ModelForm):
    class Meta:
        model = AITool
        fields = ['name', 'description', 'model_file', 'usage_instructions']

# Form for AI Question
class AIQuestionForm(forms.ModelForm):
    class Meta:
        model = AIQuestion
        fields = ['question']

# Form for AI Answer
class AIAnswerForm(forms.ModelForm):
    class Meta:
        model = AIAnswer
        fields = ['question', 'answer']

# Form for AI Result
class AIResultForm(forms.ModelForm):
    class Meta:
        model = AIResult
        fields = ['model', 'result_data']
