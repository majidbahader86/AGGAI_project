from django.db import models
from django.contrib.auth.models import User

# Model for Monitoring Data
class MonitoringData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()

    def __str__(self):
        return f"Monitoring Data at {self.timestamp}"

# Model for Monitoring Alerts
class MonitoringAlert(models.Model):
    alert_type = models.CharField(max_length=100)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Monitoring Alert - {self.alert_type}"

# Model for Monitoring Actions
class MonitoringAction(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Model for Forum Posts
class ForumPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model for Forum Comments
class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

# Model for Seasonal Alerts
class SeasonAlert(models.Model):
    crop = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=100)
    alert_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop} Alert - {self.alert_type}"

# Model for Environmental Conditions
class EnvironmentalCondition(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    alert_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Environmental Condition at {self.timestamp}"

# Model for Care Tips
class CareTip(models.Model):
    crop = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    tip = models.TextField()

    def __str__(self):
        return f"Care Tip for {self.crop} in {self.region}"

# Model for European Diseases
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

# Model for Financial Aid
class FinancialAid(models.Model):
    crop = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    def __str__(self):
        return f"{self.crop} - {self.transaction_date}"