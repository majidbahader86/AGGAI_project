from django.contrib import admin
from .models import (
    MonitoringData, MonitoringAlert, MonitoringAction,
    ForumPost, ForumComment, SeasonAlert,
    EnvironmentalCondition, CareTip, FinancialAid,
)



@admin.register(MonitoringData)
class MonitoringDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity', 'soil_moisture')
    list_filter = ('timestamp',)

@admin.register(MonitoringAlert)
class MonitoringAlertAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'created_at')
    list_filter = ('created_at',)

@admin.register(MonitoringAction)
class MonitoringActionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'content')

@admin.register(ForumComment)
class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'user', 'post__title')
    search_fields = ('content',)

@admin.register(SeasonAlert)
class SeasonAlertAdmin(admin.ModelAdmin):
    list_display = ('crop', 'alert_type', 'created_at')
    list_filter = ('created_at', 'crop', 'alert_type')
    search_fields = ('crop', 'alert_type')

@admin.register(EnvironmentalCondition)
class EnvironmentalConditionAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity', 'soil_moisture', 'alert_message')
    list_filter = ('timestamp',)
    search_fields = ('alert_message',)

@admin.register(CareTip)
class CareTipAdmin(admin.ModelAdmin):
    list_display = ('crop', 'region', 'tip')
    search_fields = ('crop', 'region', 'tip')

@admin.register(FinancialAid)
class FinancialAidAdmin(admin.ModelAdmin):
    list_display = ('crop', 'price', 'transaction_date')
    list_filter = ('transaction_date', 'crop')
    search_fields = ('crop', 'transaction_date')



