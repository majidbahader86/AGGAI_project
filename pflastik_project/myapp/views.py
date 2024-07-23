from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Item, Image
from .forms import ImageUploadForm
from django.utils.translation import gettext as _
from .view_anonymous import analyze_image as analyze_image_anonymous
from .view_farmer import analyze_image as analyze_image_farmer
from .view_scientist import analyze_image as analyze_image_scientist
import json

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
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
            return redirect('image_detail', pk=image.pk)
    else:
        form = ImageUploadForm()
    
    return render(request, 'myapp/upload_image.html', {'form': form})
def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    
    # Simulate a scientist or farmer user
    simulate_scientist = False  # Set to True to simulate a scientist user
    simulate_farmer = True  # Set to True to simulate a farmer user
    
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

    return render(request, 'myapp/image_detail.html', context)
