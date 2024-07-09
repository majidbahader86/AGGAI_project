from django.db import models

# Model representing different categories of diseases
class DiseaseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disease Categories"

# Model representing different parts of a plant
class PlantPart(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Model representing specific diseases
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
        return f"{'Healthy' if self.is_healthy else 'Diseased'} Image of {self.plant.name}"

# Model representing diagnostic sessions
class DiagnosticSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnostic Session for {self.plant.name} by {self.user.username}"
