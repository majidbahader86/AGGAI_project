from django.db import models
from django.contrib.auth.models import User
from .models import Plant  # Assuming Plant model is defined in farmers app

# Publications Model
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
    
# Community Forum Models
class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
    
class Expert(models.Model):
    name = models.CharField(max_length=255)
    field_of_expertise = models.CharField(max_length=255)
    bio = models.TextField()
    contact_info = models.EmailField()
    photo = models.ImageField(upload_to='expert_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class DiagnosticSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)  # Assuming Plant model is defined in farmers app
    symptoms = models.TextField()
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnostic Session for {self.plant.name} by {self.user.username}"

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title
