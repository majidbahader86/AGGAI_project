from django.db import models
from django.contrib.auth.models import User

# Model for Disease Identification Requests
class DiseaseIdentificationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='disease_identification/', blank=True, null=True)
    ai_requested = models.BooleanField(default=False)

    def __str__(self):
        return f"Disease Identification Request by {self.user.username} at {self.request_time}"
      
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

