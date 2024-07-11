from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define primary key as AutoField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    llm_name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_messages = models.JSONField()  # Store messages from user as JSON (list or dictionary)
    llm_responses = models.JSONField()  # Store responses from LLM as JSON (list or dictionary)
    context = models.JSONField(blank=True, null=True)  # Optional context data

    def __str__(self):
        return f'Conversation id={self.id} with {self.llm_name} initiated by {self.user.username}'

    class Meta:
        ordering = ['-timestamp']  # Optional: specify default ordering


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

class AIToolUsage(models.Model):
    tool = models.ForeignKey(AITool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_data = models.TextField()
    result = models.TextField()
    usage_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usage of {self.tool.name} by {self.user.username} on {self.usage_date}"
