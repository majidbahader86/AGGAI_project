# urls.py
from django.urls import path
from .views import (
    create_environmental_condition,
    create_care_tip,
    create_community_post,
    create_expert_qa,
    create_season_alert,
    create_european_disease,
    create_european_region,
    create_financial_record,
    environmental_condition_list,
    care_tip_list,
    community_post_list,
    expert_qa_list,
    season_alert_list,
    european_disease_list,
    european_region_list,
    financial_record_list
)

urlpatterns = [
    path('environmental_conditions/new/', create_environmental_condition, name='create_environmental_condition'),
    path('care_tips/new/', create_care_tip, name='create_care_tip'),
    path('community_posts/new/', create_community_post, name='create_community_post'),
    path('expert_qas/new/', create_expert_qa, name='create_expert_qa'),
    path('season_alerts/new/', create_season_alert, name='create_season_alert'),
    path('european_diseases/new/', create_european_disease, name='create_european_disease'),
    path('european_regions/new/', create_european_region, name='create_european_region'),
    path('financial_records/new/', create_financial_record, name='create_financial_record'),

    path('environmental_conditions/', environmental_condition_list, name='environmental_condition_list'),
    path('care_tips/', care_tip_list, name='care_tip_list'),
    path('community_posts/', community_post_list, name='community_post_list'),
    path('expert_qas/', expert_qa_list, name='expert_qa_list'),
    path('season_alerts/', season_alert_list, name='season_alert_list'),
    path('european_diseases/', european_disease_list, name='european_disease_list'),
    path('european_regions/', european_region_list, name='european_region_list'),
    path('financial_records/', financial_record_list, name='financial_record_list'),
]
