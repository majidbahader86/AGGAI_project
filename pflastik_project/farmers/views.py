# views.py
from django.shortcuts import render, get_object_or_404, redirect
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
from .forms import (
    EnvironmentalConditionForm,
    CareTipForm,
    CommunityPostForm,
    ExpertQAForm,
    SeasonAlertForm,
    EuropeanDiseaseForm,
    EuropeanRegionForm,
    FinancialRecordForm
)

def create_environmental_condition(request):
    if request.method == 'POST':
        form = EnvironmentalConditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('environmental_condition_list')
    else:
        form = EnvironmentalConditionForm()
    return render(request, 'create_environmental_condition.html', {'form': form})

def create_care_tip(request):
    if request.method == 'POST':
        form = CareTipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('care_tip_list')
    else:
        form = CareTipForm()
    return render(request, 'create_care_tip.html', {'form': form})

def create_community_post(request):
    if request.method == 'POST':
        form = CommunityPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community_post_list')
    else:
        form = CommunityPostForm()
    return render(request, 'create_community_post.html', {'form': form})

def create_expert_qa(request):
    if request.method == 'POST':
        form = ExpertQAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expert_qa_list')
    else:
        form = ExpertQAForm()
    return render(request, 'create_expert_qa.html', {'form': form})

def create_season_alert(request):
    if request.method == 'POST':
        form = SeasonAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_alert_list')
    else:
        form = SeasonAlertForm()
    return render(request, 'create_season_alert.html', {'form': form})

def create_european_disease(request):
    if request.method == 'POST':
        form = EuropeanDiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('european_disease_list')
    else:
        form = EuropeanDiseaseForm()
    return render(request, 'create_european_disease.html', {'form': form})

def create_european_region(request):
    if request.method == 'POST':
        form = EuropeanRegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('european_region_list')
    else:
        form = EuropeanRegionForm()
    return render(request, 'create_european_region.html', {'form': form})

def create_financial_record(request):
    if request.method == 'POST':
        form = FinancialRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financial_record_list')
    else:
        form = FinancialRecordForm()
    return render(request, 'create_financial_record.html', {'form': form})

def environmental_condition_list(request):
    conditions = EnvironmentalCondition.objects.all()
    return render(request, 'environmental_condition_list.html', {'conditions': conditions})

def care_tip_list(request):
    tips = CareTip.objects.all()
    return render(request, 'care_tip_list.html', {'tips': tips})

def community_post_list(request):
    posts = CommunityPost.objects.all()
    return render(request, 'community_post_list.html', {'posts': posts})

def expert_qa_list(request):
    qas = ExpertQA.objects.all()
    return render(request, 'expert_qa_list.html', {'qas': qas})

def season_alert_list(request):
    alerts = SeasonAlert.objects.all()
    return render(request, 'season_alert_list.html', {'alerts': alerts})

def european_disease_list(request):
    diseases = EuropeanDisease.objects.all()
    return render(request, 'european_disease_list.html', {'diseases': diseases})

def european_region_list(request):
    regions = EuropeanRegion.objects.all()
    return render(request, 'european_region_list.html', {'regions': regions})

def financial_record_list(request):
    records = FinancialRecord.objects.all()
    return render(request, 'financial_record_list.html', {'records': records})
