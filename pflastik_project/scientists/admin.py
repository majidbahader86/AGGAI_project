from django.contrib import admin
from .models import Publication, ForumPost, ForumComment, Expert, DiagnosticSession, Tutorial

# Register your models here.

admin.site.register(Publication)
admin.site.register(ForumPost)
admin.site.register(ForumComment)
admin.site.register(Expert)
admin.site.register(DiagnosticSession)
admin.site.register(Tutorial)

