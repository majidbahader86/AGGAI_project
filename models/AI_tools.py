from django.db import models
from django.contrib.auth.models import User

# Model for AI Tools
class AITool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model_file = models.FileField(upload_to='ai_models/')
    usage_instructions = models.TextField()

    def __str__(self):
        return self.name

# Model for AI Questions
class AIQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question by {self.user.username} on {self.created_at}"

# Model for AI Answers
class AIAnswer(models.Model):
    question = models.OneToOneField(AIQuestion, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f"Answer to {self.question}"

# Advanced AI Models
class AIModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model_file = models.FileField(upload_to='ai_models/')

    def __str__(self):
        return self.name

# AIResult: Stores results from AI predictions or optimizations.
class AIResult(models.Model):
    model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    result_data = models.JSONField()  # Example; adjust as per your data structure

    def __str__(self):
        return f"Result from {self.model.name}"
