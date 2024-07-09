from django.db import models

    
    

# AI Tools Model- Represents AI tools with fields for name, description, model file, and usage instructions.
class AITool(models.Model):
    # Name of the AI tool
    name = models.CharField(max_length=255)
    # Description of the AI tool
    description = models.TextField()
    # File upload field for the AI model file
    model_file = models.FileField(upload_to='ai_models/')
    # Instructions on how to use the AI tool
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

# Model for AI Tools
class AITool(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    model_file = models.FileField(upload_to='ai_models/')
    usage_instructions = models.TextField()

    def __str__(self):
        return self.name

# Model for recording usage of AI tools by users
class AIToolUsage(models.Model):
    tool = models.ForeignKey(AITool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_data = models.TextField()
    result = models.TextField()
    usage_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usage of {self.tool.name} by {self.user.username} on {self.usage_date}"
    

# AIToolUsage: Records usage of AI tools by users, storing input data, results, and usage date.
class AIToolUsage(models.Model):
    # Reference to the AI tool being used
    tool = models.ForeignKey(AITool, on_delete=models.CASCADE)
    # Reference to the user who used the AI tool
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Input data provided by the user
    input_data = models.TextField()
    # Result produced by the AI tool
    result = models.TextField()
    # Date and time when the tool was used
    usage_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Usage of {self.tool.name} by {self.user.username} on {self.usage_date}"