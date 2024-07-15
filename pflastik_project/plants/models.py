# from django.db import models

# # Model representing different plant species
# class Plant(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     scientific_name = models.CharField(max_length=255)
#     description = models.TextField()
#     habitat = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name

# # Model representing images associated with specific plants
# class PlantImage(models.Model):
#     plant = models.ForeignKey(Plant, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='plant_images/')
#     description = models.CharField(max_length=255, blank=True)
#     is_healthy = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{'Healthy' if self.is_healthy else 'Diseased'} Image of {self.plant.name}"

