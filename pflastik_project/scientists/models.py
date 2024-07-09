from django.db import models
from django.contrib.auth.models import User

class Expert(models.Model):
    name = models.CharField(max_length=255)
    field_of_expertise = models.CharField(max_length=255)
    bio = models.TextField()
    contact_info = models.EmailField()
    photo = models.ImageField(upload_to='expert_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    abstract = models.TextField()
    content = models.TextField()
    published_date = models.DateField()
    category = models.CharField(max_length=255)
    file = models.FileField(upload_to='publications/')
    external_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
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