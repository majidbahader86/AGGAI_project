from django.contrib import admin
from .models import DiseaseCategory, PlantPart, DiagnosticSession

admin.site.register(DiseaseCategory)
admin.site.register(PlantPart)
admin.site.register(DiagnosticSession)