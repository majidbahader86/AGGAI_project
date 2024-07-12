from django.db import models
from django.contrib.auth.models import User

# Monitoring Models
class MonitoringData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()

    def __str__(self):
        return f"Monitoring Data at {self.timestamp}"

class MonitoringAlert(models.Model):
    alert_type = models.CharField(max_length=100)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Monitoring Alert - {self.alert_type}"

class MonitoringAction(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Forum Models
class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

# Seasonal Alerts Model
class SeasonAlert(models.Model):
    crop = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=100)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop} Alert - {self.alert_type}"

# Environmental Conditions Model
class EnvironmentalCondition(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    alert_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Environmental Condition at {self.timestamp}"

# Care Tips Model
class CareTip(models.Model):
    crop = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    tip = models.TextField()

    def __str__(self):
        return f"Care Tip for {self.crop} in {self.region}"

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

# Financial Aid Model
class FinancialAid(models.Model):
    crop = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    def __str__(self):
        return f"{self.crop} - {self.transaction_date}"

# AI Tool Models

class AITool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model_file = models.FileField(upload_to='ai_models/')
    usage_instructions = models.TextField()

    def __str__(self):
        return self.name

class AIQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question by {self.user.username} on {self.created_at}"

class AIAnswer(models.Model):
    question = models.OneToOneField(AIQuestion, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f"Answer to {self.question}"

class AIResult(models.Model):
    model = models.ForeignKey(AITool, on_delete=models.CASCADE)
    result_data = models.JSONField()  # Example; adjust as per your data structure

    def __str__(self):
        return f"Result from {self.model.name}"