from django.db import models

# Model representing different categories of diseases such as fungal, bacterial, etc.
class DiseaseCategory(models.Model):
    # Name of the disease category
    name = models.CharField(max_length=255, unique=True)
    # Optional description of the disease category
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disease Categories"


# Model representing different parts of a plant that can be affected by diseases
class PlantPart(models.Model):
    # Name of the plant part, e.g., leaf, stem, root
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Model representing specific diseases with detailed information
class Disease(models.Model):
    
    # Name of the disease
    name = models.CharField(max_length=255, unique=True)
    
    # Category of the disease (e.g., fungal, bacterial), linked to DiseaseCategory
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)
    
    # Detailed description of the disease
    description = models.TextField()
    
    # Symptoms of the disease
    symptoms = models.TextField()
    
    # Treatment methods for the disease
    treatment = models.TextField()
    
    # Prevention methods for the disease
    prevention = models.TextField()
    
    # Plant parts affected by the disease, linked to PlantPart
    affected_parts = models.ManyToManyField(PlantPart, related_name='diseases')

    def __str__(self):
        return self.name


# Model representing images associated with specific diseases

class DiseaseImage(models.Model):
    # The disease the image is associated with, linked to Disease
    disease = models.ForeignKey(Disease, related_name='images', on_delete=models.CASCADE)
    # Image file
    image = models.ImageField(upload_to='disease_images/')
    # Optional description of the image
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image of {self.disease.name}"


# Model representing different plant species
class Plant(models.Model):
    # Name of the plant
    name = models.CharField(max_length=255, unique=True)
    # Detailed description of the plant
    description = models.TextField()

    def __str__(self):
        return self.name


# Model representing images associated with specific plants
class PlantImage(models.Model):
    # The plant the image is associated with, linked to Plant
    plant = models.ForeignKey(Plant, related_name='images', on_delete=models.CASCADE)
    # Image file
    image = models.ImageField(upload_to='plant_images/')
    # Optional description of the image
    description = models.CharField(max_length=255, blank=True)
    # Boolean indicating whether the image shows a healthy plant
    is_healthy = models.BooleanField(default=True)

    def __str__(self):
        if self.is_healthy:
            return f"Healthy Image of {self.plant.name}"
        else:
            return f"Diseased Image of {self.plant.name}"
        
        # Plant Database Models
class Plant(models.Model):
    # Common name of the plant
    name = models.CharField(max_length=255, unique=True)
    # Scientific name of the plant
    scientific_name = models.CharField(max_length=255)
    # Description of the plant
    description = models.TextField()
    # Natural habitat of the plant
    habitat = models.CharField(max_length=255)
    # Reference to multiple images of the plant
    images = models.ManyToManyField('PlantImage', related_name='plants')

    def __str__(self):
        return self.name
