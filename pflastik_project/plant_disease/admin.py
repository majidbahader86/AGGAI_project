from django.contrib import admin
from .models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant, PlantImage

# Register your models here.
admin.site.register(DiseaseCategory)
admin.site.register(PlantPart)
admin.site.register(Disease)
admin.site.register(DiseaseImage)
admin.site.register(EuropeanDisease)
admin.site.register(Plant)
admin.site.register(PlantImage)
