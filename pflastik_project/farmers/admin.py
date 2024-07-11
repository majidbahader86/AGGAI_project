from django.contrib import admin
from .models import DiseaseIdentificationRequest, ForumPost, ForumComment, SeasonAlert

admin.site.register(DiseaseIdentificationRequest)
admin.site.register(ForumPost)
admin.site.register(ForumComment)
admin.site.register(SeasonAlert)

