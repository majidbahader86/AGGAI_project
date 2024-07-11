# forms.py
from django import forms
from .models import (
    EnvironmentalCondition,
    CareTip,
    CommunityPost,
    ExpertQA,
    SeasonAlert,
    EuropeanDisease,
    EuropeanRegion,
    FinancialRecord
)

class EnvironmentalConditionForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalCondition
        fields = ['temperature', 'humidity', 'soil_moisture', 'alert_message']

class CareTipForm(forms.ModelForm):
    class Meta:
        model = CareTip
        fields = ['crop', 'region', 'tip']

class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['title', 'content']

class ExpertQAForm(forms.ModelForm):
    class Meta:
        model = ExpertQA
        fields = ['expert_name', 'question', 'answer']

class SeasonAlertForm(forms.ModelForm):
    class Meta:
        model = SeasonAlert
        fields = ['crop', 'alert_type', 'alert_message']

class EuropeanDiseaseForm(forms.ModelForm):
    class Meta:
        model = EuropeanDisease
        fields = ['name', 'category', 'description', 'symptoms', 'treatment', 'prevention', 'affected_parts']

class EuropeanRegionForm(forms.ModelForm):
    class Meta:
        model = EuropeanRegion
        fields = ['name', 'boundary']

class FinancialRecordForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = ['crop', 'price', 'transaction_date']
