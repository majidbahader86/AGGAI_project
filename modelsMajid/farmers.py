from django.db import models
from django.contrib.auth.models import User

# Model for monitoring environmental conditions- This model stores data related to environmental conditions such as temperature, humidity, and soil moisture. It includes an optional field for alert messages.
class EnvironmentalCondition(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    alert_message = models.TextField(blank=True, null=True)
    # Other fields as needed

    def __str__(self):
        return f"Environmental Condition at {self.timestamp}"


# Model for storing care tips- Stores care tips specific to crops and regions, providing personalized recommendations to users.
class CareTip(models.Model):
    crop = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    tip = models.TextField()

    def __str__(self):
        return f"Care Tip for {self.crop} in {self.region}"
    

# Model for community posts- Represents posts made by users in the community section, facilitating interactions and discussions among farmers.
class CommunityPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Model for expert Q&A sessions- Stores questions and answers from expert sessions, where agricultural experts provide insights and advice.
class ExpertQA(models.Model):
    expert_name = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question[:50]}..."


# Model for seasonal alerts- Stores alerts related to weather forecasts and crop-specific conditions, helping farmers stay informed about potential risks or opportunities.
class SeasonAlert(models.Model):
    crop = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=100)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop} Alert - {self.alert_type}"
    
    
    # Catalog diseases affecting crops in Europe, along with specific prevention and treatment methods.
    class EuropeanDisease(models.Model):
     name = models.CharField(max_length=255, unique=True)
     category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)
     description = models.TextField()
     symptoms = models.TextField()
     treatment = models.TextField()
     prevention = models.TextField()
     affected_parts = models.ManyToManyField(PlantPart, related_name='european_diseases')
    # Add more fields as needed for European disease details
    
    def __str__(self):
        return self.name
    
    
    
from django.contrib.gis.db import models as gis_models

# Store geographical boundaries of European regions for precise mapping and analysis.
class EuropeanRegion(models.Model):
    name = models.CharField(max_length=255)
    boundary = gis_models.MultiPolygonField()  # Represents boundaries of European regions
    # Add more fields as needed for European regions
    
    def __str__(self):
        return self.name
    

# FinancialRecord: Stores financial data related to crop pricing, budgeting, etc
class FinancialRecord(models.Model):
    crop = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    # Add more fields for financial details
    
    def __str__(self):
        return f"{self.crop} - {self.transaction_date}"
