# models.py
from django.db import models
from django.contrib.auth.models import User
from plant_disease.models import Disease

class DiseaseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disease Categories"
        
    @staticmethod
    def prepopulate():
        categories = [
            {"name": "Fungal", "description": "Diseases caused by fungi"},
            {"name": "Bacterial", "description": "Diseases caused by bacteria"},
            {"name": "Viral", "description": "Diseases caused by viruses"},
            {"name": "Nematode", "description": "Diseases caused by nematodes"},
            {"name": "Physiological", "description": "Non-infectious diseases caused by environmental factors"}
        ]
        for category in categories:
            DiseaseCategory.objects.get_or_create(**category)

# Model representing different parts of a plant that can be affected by diseases
class PlantPart(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    @staticmethod
    def prepopulate():
        parts = [
            {"name": "Stem"},
            {"name": "Root"},
            {"name": "Leaves"},
            {"name": "Seeds"},
            {"name": "Flowers"}
        ]
        for part in parts:
            PlantPart.objects.get_or_create(**part)

# Model representing specific diseases with detailed information

class DiagnosticSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(PlantPart, on_delete=models.CASCADE)  # Adjust based on your actual Plant model
    symptoms = models.TextField()
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnostic Session for {self.plant.name} by {self.user.username}"


