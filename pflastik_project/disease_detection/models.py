# models.py
from django.db import models
from django.contrib.auth.models import User



class DiseaseIdentificationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='disease_identification/', blank=True, null=True)
    ai_requested = models.BooleanField(default=False)

    def __str__(self):
        return f"Disease Identification Request by {self.user.username} at {self.request_time}"




