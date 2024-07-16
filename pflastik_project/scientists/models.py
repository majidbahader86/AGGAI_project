from django.db import models
from django.contrib.auth.models import User as DjangoUser


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

from django.contrib.auth.models import User  # Import User model from django.contrib.auth
from plant_disease.models import PlantPart 

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