from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PublicationForm, ForumPostForm, ForumCommentForm, ExpertForm, DiagnosticSessionForm, TutorialForm, ScientistSignInForm, ScientistSignUpForm,  DiseaseReportForm, SciencePaperForm, DatasetForm, ImageUploadForm
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial , SciencePaper, PlantsDataset, AgentResponse ,Item, Image
from django.http import JsonResponse , HttpResponse
from django.conf import settings
from django.utils.translation import gettext as _
from .Agents.view_farmer import analyze_image as analyze_image_farmer
from .Agents.view_scientist import analyze_image as analyze_image_scientist
from .Agents.view_anonymous import analyze_image as analyze_image_anonymous
from .Agents.ai_framework import get_agents
from django.views.decorators.csrf import csrf_exempt
import json

def report_form(request):
    context = {
        'disease_form': DiseaseReportForm(),
        'paper_form': SciencePaperForm(),
        'dataset_form': DatasetForm()
    }
    return render(request, 'report_form.html', context)

@csrf_exempt
def submit_disease_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = DiseaseReportForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Disease information submitted successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def submit_paper_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = SciencePaperForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Paper information submitted successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def submit_dataset_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = DatasetForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Dataset information submitted successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=True)
            user = request.user

            if user.is_authenticated:
                if user.groups.filter(name='Farmers').exists():
                    analysis = analyze_image_farmer(image.image.path)
                elif user.groups.filter(name='Scientists').exists():
                    analysis = analyze_image_scientist(image.image.path)
                else:
                    analysis = analyze_image_anonymous(image.image.path)
            else:
                analysis = analyze_image_anonymous(image.image.path)
            
            image.analysis = json.dumps(analysis)  # Convert analysis to JSON string
            image.save()
            return redirect('image_details', pk=image.pk)
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload_image.html', {'form': form})

def image_details(request, pk):
    image = get_object_or_404(Image, pk=pk)
    
    # Simulate a scientist or farmer user
    simulate_scientist = True  # Set to True to simulate a scientist user
    simulate_farmer = False 
    
    class FakeGroup:
        def __init__(self, name):
            self.name = name

    class FakeUser:
        def __init__(self, is_authenticated, groups):
            self.is_authenticated = is_authenticated
            self.groups = groups

        def groups_filter(self, name):
            return [group for group in self.groups if group.name == name]

    if simulate_scientist:
        user = FakeUser(True, [FakeGroup('Scientists')])
    elif simulate_farmer:
        user = FakeUser(True, [FakeGroup('Farmers')])
    else:
        user = request.user

    if user.is_authenticated:
        if isinstance(user, FakeUser):
            is_farmer = bool(user.groups_filter('Farmers'))
            is_scientist = bool(user.groups_filter('Scientists'))
        else:
            is_farmer = user.groups.filter(name='Farmers').exists()
            is_scientist = user.groups.filter(name='Scientists').exists()

        if is_farmer:
            user_role = 'farmer'
            page_title = _('Farmer Image Analysis')
            analysis_json = analyze_image_farmer(image.image.path)
        elif is_scientist:
            user_role = 'scientist'
            page_title = _('Scientist Image Analysis')
            analysis_json = analyze_image_scientist(image.image.path)
        else:
            user_role = 'authenticated'
            page_title = _('Authenticated User Image Analysis')
            analysis_json = analyze_image_anonymous(image.image.path)
    else:
        user_role = 'anonymous'
        page_title = _('Anonymous User Image Details')
        analysis_json = analyze_image_anonymous(image.image.path)

    # Parse the JSON string into a Python dictionary
    try:
        analysis = json.loads(analysis_json)
    except json.JSONDecodeError:
        print(f"Failed to parse analysis JSON for image {pk}. Using empty dictionary.")
        analysis = {}

    context = {
        'image': image,
        'page_title': page_title,
        'user_role': user_role,
        'analysis': analysis,
    }
    print(f"Image path: {image.image.path}")
    print(f"Image URL: {image.image.url}")

    return render(request, 'image_details.html', context)

def chain_agent(request):
    agent = {
        'icon_path': 'M12 2L2 7v10l10 5 10-5V7L12 2zm0 18.5l-8-4V8.5l8 4v8zm0-10l-8-4L12 3l8 3.5-8 4zm8 6v-8l-8 4v8l8-4z',
        'title': 'AI Agent Dashboard',
        'status': 'Active and Synced',
        'button_text': 'View AI Agent Details'
    }
    
    chains = [
        {'name': 'PlantChain', 'status': 'Connected', 'status_class': 'connected'},
        {'name': 'Genetic Chain', 'status': 'Synced', 'status_class': 'synced'}
    ]
    
    stats = [
        {'label': 'Plant Analysis Accuracy', 'value': '98.5%', 'id': 'accuracy'},
        {'label': 'Genetic Sequences Processed', 'value': '1,440', 'id': 'tasks'},
        {'label': 'AI System Uptime', 'value': '99.58%', 'id': 'uptime'}
    ]
    
    tables = [
        {
            'title': 'PlantChain Blocks (Plant Disease Analysis)',
            'id': 'plantchain-table',
            'headers': ['Block Number', 'Hash', 'Plant Diseases Analyzed', 'Research Papers Referenced', 'Genetic Data Sets Processed'],
            'body_id': 'plantchain-blocks'
        },
        {
            'title': 'GeneChain Blocks (Genetic Sequencing)',
            'id': 'genechain-table',
            'headers': ['Block Number', 'Hash', 'Genetic Sequences', 'Species Analyzed'],
            'body_id': 'genechain-blocks'
        }
    ]
    
    return render(request, 'chain_agent.html', {'agent': agent, 'chains': chains, 'stats': stats, 'tables': tables})


def dashboard(request):
    # Example data, replace these with actual queries
    current_research = {
        'title': 'Gene editing in drought-resistant crops',
        'progress': 75
    }
    
    publications = SciencePaper.objects.all()[:5]  # Get the first 5 publications
    
    funding_status = {
        'title': 'Federal Grant for Sustainable Agriculture',
        'utilization': 45
    }
    
    project_pipeline = [
        {'name': 'Soil Health Improvement', 'priority': 'High'},
        {'name': 'Climate-Resilient Varieties', 'priority': 'Medium'},
        {'name': 'Urban Farming Initiatives', 'priority': 'Low'}
    ]
    
    lab_equipment = {
        'name': 'Greenhouse Sensors',
        'functional_status': 80,
        'status_class': 'available',  # This can be 'available', 'partial', 'high', etc.
        'status_text': 'Available'
    }
    
    team_meetings = [
        {'name': 'Next Meeting', 'date': '10th July 2023'},
        {'name': 'Project Sync', 'date': '12th July 2023'},
        {'name': 'Research Workshop', 'date': '20th July 2023'}
    ]
    
    blockchain_info = {
        'public_key': '1234abcd5678efgh9012ijkl3456mnop',
        'private_key': 'mnop3456ijkl9012efgh5678abcd1234',
        'encryption_status': 'All research data is encrypted using AES-256 for maximum security.',
        'last_check': '1st July 2023'
    }

    context = {
        'current_research': current_research,
        'publications': publications,
        'funding_status': funding_status,
        'project_pipeline': project_pipeline,
        'lab_equipment': lab_equipment,
        'team_meetings': team_meetings,
        'blockchain_info': blockchain_info,
    }
    
    return render(request, 'dashboard.html', context)

def blockchain(request):
    cards = [
        {
            'gradient_class': 'gradient-plant-disease',
            'icon_path': 'M19 3H5c-1.1 0-1.99.9-1.99 2L3 19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-1 11h-4v4h-4v-4H6v-4h4V6h4v4h4v4z',
            'title': 'Plant Disease Data',
            'subtitle1': 'Total records',
            'value1': '125,000',
            'subtitle2': 'Latest update',
            'value2': '2 hours ago',
            'progress': 75
        },
        {
            'gradient_class': 'gradient-scientific-papers',
            'icon_path': 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z',
            'title': 'Scientific Papers',
            'subtitle1': 'Published this month',
            'value1': '87',
            'subtitle2': 'Total in database',
            'value2': '15,423',
            'progress': 65
        },
        {
            'gradient_class': 'gradient-datasets',
            'icon_path': 'M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z',
            'title': 'Datasets',
            'subtitle1': 'New datasets',
            'value1': '45',
            'subtitle2': 'Total available',
            'value2': '2,564',
            'progress': 90
        }
    ]
    
    charts = [
        {
            'gradient_class': 'gradient-disease-identifier',
            'agent_logo': 'DI',
            'agent_title': 'Disease Identifier Agent (LLama3.1 405B)',
            'agent_description': 'Diagnosing diseases from Plant Chain.',
            'chart_id': 'diseaseChart'
        },
        {
            'gradient_class': 'gradient-publication-analyzer',
            'agent_logo': 'PA',
            'agent_title': 'Publication Analyzer (GPT-4 512B)',
            'agent_description': 'AI agent for analyzing and summarizing scientific papers in plant science.',
            'chart_id': 'paperChart'
        },
        {
            'gradient_class': 'gradient-dataset-distributor',
            'agent_logo': 'DD',
            'agent_title': 'Dataset Distributor (BERT 345M)',
            'agent_description': 'AI agent for organizing and distributing plant science datasets efficiently.',
            'chart_id': 'datasetChart'
        },
        {
            'gradient_class': 'gradient-variety-comparator',
            'agent_logo': 'VC',
            'agent_title': 'Variety Comparator (XGBoost 128M)',
            'agent_description': 'AI agent for comparing and analyzing different plant varieties.',
            'chart_id': 'newChart'
        }
    ]
    
    return render(request, 'blockchain.html', {'cards': cards, 'charts': charts})

@login_required
def publication_create_view(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Replace 'publication_list' with your publication list URL name
    else:
        form = PublicationForm()
    return render(request, 'publication_create.html', {'form': form})

@login_required
def publication_update_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publication_list')  # Replace 'publication_list' with your publication list URL name
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'publication_update.html', {'form': form})

@login_required
def publication_delete_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')  # Replace 'publication_list' with your publication list URL name
    return render(request, 'publication_delete.html', {'publication': publication})

@login_required
def forum_post_create_view(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_post_list')  # Replace 'forum_post_list' with your forum post list URL name
    else:
        form = ForumPostForm()
    return render(request, 'forum_post_create.html', {'form': form})

@login_required
def forum_comment_create_view(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('forum_post_detail', post_id=post_id)  # Replace 'forum_post_detail' with your forum post detail URL name
    else:
        form = ForumCommentForm()
    return render(request, 'forum_comment_create.html', {'form': form, 'post': post})

@login_required
def expert_create_view(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('expert_list')  # Replace 'expert_list' with your expert list URL name
    else:
        form = ExpertForm()
    return render(request, 'expert_create.html', {'form': form})

@login_required
def diagnostic_session_create_view(request):
    if request.method == 'POST':
        form = DiagnosticSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnostic_session_list')  # Replace 'diagnostic_session_list' with your diagnostic session list URL name
    else:
        form = DiagnosticSessionForm()
    return render(request, 'diagnostic_session_create.html', {'form': form})

@login_required
def tutorial_create_view(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')  # Replace 'tutorial_list' with your tutorial list URL name
    else:
        form = TutorialForm()
    return render(request, 'tutorial_create.html', {'form': form})

def scientist_signin_view(request):
    if request.method == 'POST':
        form = ScientistSignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace 'dashboard' with your scientist dashboard URL name
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = ScientistSignInForm()
    return render(request, 'scientist_signin.html', {'form': form})

def scientist_signup_view(request):
    if request.method == 'POST':
        form = ScientistSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your scientist dashboard URL name
    else:
        form = ScientistSignUpForm()
    return render(request, 'scientist_signup.html', {'form': form})

@login_required
def publication_combined_view(request, pk=None, action=None):
    if pk:
        publication = get_object_or_404(Publication, pk=pk)
    else:
        publication = None

    if request.method == 'POST':
        if action == 'delete' and publication:
            publication.delete()
            return redirect('publication_list')  # Replace with your publication list URL name
        else:
            form = PublicationForm(request.POST, request.FILES, instance=publication)
            if form.is_valid():
                form.save()
                return redirect('publication_list')  # Replace with your publication list URL name
    else:
        form = PublicationForm(instance=publication)

    publications = Publication.objects.all()
    return render(request, 'publications.html', {
        'form': form,
        'publication': publication,
        'publications': publications,
        'action': action
    })

@login_required
def tutorial_combined_view(request, pk=None):
    if pk:
        tutorial = get_object_or_404(Tutorial, pk=pk)
    else:
        tutorial = None

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES, instance=tutorial)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')  
    else:
        form = TutorialForm(instance=tutorial)

    return render(request, 'tutorials.html', {'form': form, 'tutorial': tutorial})

def ai_framework(request):
    agents = get_agents()
    return render(request, 'ai_framework.html', {'agents': agents})

def test(request):
    return render(request, 'test.html')

def my_plants(request):
    return render(request, 'my_plants.html')

def experiments(request):
    return render(request, 'experiments.html')

def publications(request):
    return render(request, 'publications.html')

def tutorials(request):
    return render(request, 'tutorials.html')

def settings(request):
    return render(request, 'settings.html')

def docs(request):
    return render(request, 'docs.html')
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def agent_view(request, agent_name):
    # Use agent_name to determine which template or data to provide
    return render(request, 'agent_page.html', {'agent_name': agent_name})

def disease_identifier(request):
    return render(request, 'disease_identifier.html')