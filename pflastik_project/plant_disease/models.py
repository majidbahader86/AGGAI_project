from django.db import models

# Model representing different categories of diseases such as fungal, bacterial, etc.
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
class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)
    description = models.TextField()
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    affected_parts = models.ManyToManyField(PlantPart, related_name='diseases')

    def __str__(self):
        return self.name

# Model representing images associated with specific diseases
class DiseaseImage(models.Model):
    disease = models.ForeignKey(Disease, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='disease_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image of {self.disease.name}"

# European Diseases Model
class EuropeanDisease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)
    description = models.TextField()
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    affected_parts = models.ManyToManyField(PlantPart, related_name='european_diseases')

    def __str__(self):
        return self.name

# Model representing different plant species
class Plant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    scientific_name = models.CharField(max_length=255)
    description = models.TextField()
    habitat = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Model representing images associated with specific plants
class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plant_images/')
    description = models.CharField(max_length=255, blank=True)
    is_healthy = models.BooleanField(default=True)

    def __str__(self):
        if self.is_healthy:
            return f"Healthy Image of {self.plant.name}"
        else:
            return f"Diseased Image of {self.plant.name}"
