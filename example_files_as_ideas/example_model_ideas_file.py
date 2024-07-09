
#These classes will all be separate .py files within 'models'
#  1. file with shared model(both for scientific and farmer categories) called common.py
from django.db import models

class PlantDisease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    symptoms = models.TextField()
    causes = models.TextField()
    prevention = models.TextField()

    def __str__(self):
        return self.name

# 2. file with scientist model:
from django.db import models
from .common import PlantDisease

# a file with the scientist user model

class ScientistInfo(models.Model):
    disease = models.ForeignKey(PlantDisease, on_delete=models.CASCADE)
    research_papers = models.TextField()
    advanced_studies = models.TextField()
    laboratory_results = models.TextField()

    def __str__(self):
        return f"Scientist Info for {self.disease.name}"

# 3. file with the farmer user model
from django.db import models
from .common import PlantDisease

class ScientistInfo(models.Model):
    disease = models.ForeignKey(PlantDisease, on_delete=models.CASCADE)
    research_papers = models.TextField()
    advanced_studies = models.TextField()
    laboratory_results = models.TextField()

    def __str__(self):
        return f"Scientist Info for {self.disease.name}"
