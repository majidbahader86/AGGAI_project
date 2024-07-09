# models.py
from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('disease_detection.DiseaseCategory', on_delete=models.CASCADE)
    description = models.TextField()
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    affected_parts = models.ManyToManyField('disease_detection.PlantPart', related_name='diseases')

    def __str__(self):
        return self.name

class DiseaseImage(models.Model):
    disease = models.ForeignKey(Disease, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='disease_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image of {self.disease.name}"

class SeasonAlert(models.Model):
    crop = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=100)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop} Alert - {self.alert_type}"


