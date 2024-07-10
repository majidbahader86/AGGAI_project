# views.py

from django.shortcuts import render, get_object_or_404
from .models import Expert, Publication, Tutorial

# Expert views
def expert_list(request):
    experts = Expert.objects.all()
    return render(request, 'expert_list.html', {'experts': experts})

def expert_detail(request, pk):
    expert = get_object_or_404(Expert, pk=pk)
    return render(request, 'expert_detail.html', {'expert': expert})

# Publication views
def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'publication_list.html', {'publications': publications})

def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publication_detail.html', {'publication': publication})

# Tutorial views
def tutorial_list(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial_list.html', {'tutorials': tutorials})

def tutorial_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'tutorial_detail.html', {'tutorial': tutorial})
