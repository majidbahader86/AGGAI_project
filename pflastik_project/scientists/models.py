from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.contrib.postgres.fields import JSONField
import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from plant_disease.models import PlantPart 
from django.contrib.auth.models import User


def generate_unique_id():
    return str(uuid.uuid4())[:8]

def generate_unique_id_with_prefix(prefix, model):
    while True:
        unique_id = f"{prefix}-{generate_unique_id()}"
        if not model.objects.filter(**{model.ID_FIELD_NAME: unique_id}).exists():
            return unique_id


# Publications Model- Manages research papers and articles with fields for title, author, abstract, content, published date, category, and file upload.
# Publications Model
class Publication(models.Model):
    # Title of the publication
    title = models.CharField(max_length=255)
    # Author of the publication
    author = models.CharField(max_length=255)
    # Abstract/summary of the publication
    abstract = models.TextField()
    # Full content of the publication
    content = models.TextField()
    # Date when the publication was published
    published_date = models.DateField()
    # Category of the publication (e.g., research paper, article)
    category = models.CharField(max_length=255)
    # File upload field for the publication document
    file = models.FileField(upload_to='publications/')
    # URL for external resources or references
    external_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analysis = models.TextField(blank=True)

    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"
    

# Community Forum Models
class ForumPost(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='scientists_forum_posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='scientists_forum_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

    

# Expert: Directory of experts with fields for name, field of expertise, bio, contact info, and photo.
# Expert Directory Model
class Expert(models.Model):
    # Name of the expert
    name = models.CharField(max_length=255)
    # Field of expertise of the expert
    field_of_expertise = models.CharField(max_length=255)
    # Bio or profile of the expert
    bio = models.TextField()
    # Contact information of the expert
    contact_info = models.EmailField()
    # Photo of the expert
    photo = models.ImageField(upload_to='expert_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


# Diagnostic Tools Model- Records diagnostic sessions with user and plant references, symptoms, diagnosis result, and creation date.
# scientists/models.py


class DiagnosticSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(PlantPart, on_delete=models.CASCADE)  # Adjust based on your actual Plant model
    symptoms = models.TextField()
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnostic Session for {self.plant.name} by {self.user.username}"

# Tutorials and Guides Model- Manages tutorials and guides with fields for title, content, creation date, last updated date, and category.
class Tutorial(models.Model):
    # Title of the tutorial
    title = models.CharField(max_length=255)
    # Content of the tutorial
    content = models.TextField()
    # Date and time when the tutorial was created
    created_at = models.DateTimeField(auto_now_add=True)
    # Date and time when the tutorial was last updated
    updated_at = models.DateTimeField(auto_now=True)
    # Category of the tutorial (e.g., plant care, disease treatment)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
# it will be better if you remove the entire chain form the system and make all ops parallel 
    
class DiseaseReport(models.Model):
    ID_FIELD_NAME = 'disease_id'
    disease_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    plant_type = models.CharField(max_length=100)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    date_of_incident = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    submitted_by = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    severity = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High'), ('Severe', 'Severe')], blank=True, null=True)
    environmental_conditions = models.JSONField(blank=True, null=True)

class SciencePaper(models.Model):
    ID_FIELD_NAME = 'paper_id'
    paper_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title = models.CharField(max_length=255)
    authors = models.JSONField(default=list)
    abstract = models.TextField()
    publication_date = models.DateField()
    journal = models.CharField(max_length=255, default='Unknown Journal')
    url = models.URLField(default='http://example.com')  
    keywords = models.JSONField(default=list, blank=True, null=True)
    citation_count = models.IntegerField(default=0)
    related_topics = models.JSONField(default=list, blank=True, null=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    research_field = models.CharField(max_length=255, blank=True, null=True)
    methodology = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class PlantsDataset(models.Model):
    ID_FIELD_NAME = 'dataset_id'
    dataset_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField()
    creation_date = models.DateField()
    url = models.URLField()
    creator = models.CharField(max_length=255)
    data_format = models.CharField(max_length=50, blank=True, null=True)
    size_bytes = models.BigIntegerField(default=0)
    license = models.CharField(max_length=255, blank=True, null=True)
    tags = models.JSONField(default=list, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    data_sources = models.JSONField(default=list, blank=True, null=True)
    data_quality_metrics = models.JSONField(default=dict)
    hash_value = models.CharField(max_length=255, blank=True, null=True)

@receiver(pre_save, sender=DiseaseReport)
def set_disease_report_id(sender, instance, **kwargs):
    if not instance.disease_id:
        instance.disease_id = generate_unique_id_with_prefix('DR', DiseaseReport)

@receiver(pre_save, sender=SciencePaper)
def set_science_paper_id(sender, instance, **kwargs):
    if not instance.paper_id:
        instance.paper_id = generate_unique_id_with_prefix('SP', SciencePaper)

@receiver(pre_save, sender=PlantsDataset)
def set_plants_dataset_id(sender, instance, **kwargs):
    if not instance.dataset_id:
        instance.dataset_id = generate_unique_id_with_prefix('PD', PlantsDataset)

class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class SearchResult(models.Model):
    query = models.ForeignKey(SearchQuery, related_name='results', on_delete=models.CASCADE)
    summary = models.TextField()
    topics = models.TextField()
    relevance = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class AgentResponse(models.Model):
    block_index = models.IntegerField()
    search_term = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    final_summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)