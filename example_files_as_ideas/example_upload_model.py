from django.db import models

class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"
