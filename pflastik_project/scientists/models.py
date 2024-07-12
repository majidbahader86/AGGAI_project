from django.db import models
from django.contrib.auth.models import User


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
# ForumPost: Represents a forum post with a user reference, title, content, and creation date.
class ForumPost(models.Model):
    # Reference to the user who created the post
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Title of the forum post
    title = models.CharField(max_length=255)
    # Content of the forum post
    content = models.TextField()
    # Date and time when the post was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
# ForumComment: Represents comments on forum posts with a user reference, post reference, content, and creation date.
class ForumComment(models.Model):
    # Reference to the forum post being commented on
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    # Reference to the user who made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Content of the comment
    content = models.TextField()
    # Date and time when the comment was created
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
class DiagnosticSession(models.Model):
    # Reference to the user who created the diagnostic session
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Reference to the plant being diagnosed
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    # Symptoms provided by the user for diagnosis
    symptoms = models.TextField()
    # Diagnosis result
    diagnosis = models.TextField()
    # Date and time when the diagnostic session was created
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