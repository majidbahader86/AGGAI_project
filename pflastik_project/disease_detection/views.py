from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiseaseIdentificationRequest
from .forms import DiseaseIdentificationRequestForm

# View to create a new disease identification request
@login_required
def create_disease_identification_request(request):
    if request.method == 'POST':
        form = DiseaseIdentificationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            disease_request = form.save(commit=False)
            disease_request.user = request.user
            disease_request.save()
            return redirect('list_disease_identification_requests')
    else:
        form = DiseaseIdentificationRequestForm()
    return render(request, 'create_disease_identification_request.html', {'form': form})

# View to list all disease identification requests for the logged-in user
@login_required
def list_disease_identification_requests(request):
    disease_requests = DiseaseIdentificationRequest.objects.filter(user=request.user)
    return render(request, 'list_disease_identification_requests.html', {'disease_requests': disease_requests})