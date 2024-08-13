from django.urls import path
from django.conf.urls.static import static
from .Agents import swarm_agents_views , search_agents_views
from .views import (
    chain_agent,
    scientist_signup_view,
    scientist_signin_view,
    dashboard,
    my_plants,
    experiments,
    publications,
    blockchain,
    ai_framework,
    tutorials,
    settings,
    docs,
    test,
    agent_view,
    disease_identifier,
    upload_image,
    image_details,
    publication_combined_view,
    tutorial_combined_view,
    report_form,
    submit_disease_info,
    submit_paper_info,
    submit_dataset_info,
    chain_agent   
)

urlpatterns = [
    path('signup/', scientist_signup_view, name='scientist_sign_up'),
    path('login/', scientist_signin_view, name='scientist_log_in'),
    path('dashboard/', dashboard, name='scientist_dashboard'),
    path('my-plants/', my_plants, name='scientist_my_plants'),
    path('experiments/', experiments, name='scientist_experiments'),
    path('publications/', publications, name='scientist_publications'),
    path('blockchain/', blockchain, name='scientist_blockchain'),
    path('ai_framework/', ai_framework, name='scientist_ai_framework'),
    path('tutorials/', tutorials, name='scientist_tutorials'),
    path('settings/', settings, name='scientist_settings'),
    path('docs/', docs, name='scientist_docs'),
    path('test/', test, name='scientist_test'),
    path('chain_agent/', chain_agent, name='chain_agent'),
    path('scientists/<str:agent_name>/', agent_view, name='chain_agent'),
    path('disease_identifier/', disease_identifier, name='disease_identifier'),
    path('image/<int:pk>/', image_details, name='image_details'),
    path('upload_image/', upload_image, name='upload_image'),
    path('publications/', publication_combined_view, name='publication_create'),  
    path('publications/<int:pk>/', publication_combined_view, name='publication_update'),  
    path('publications/<int:pk>/<str:action>/', publication_combined_view, name='publication_combined'), 
    path('tutorial/new/', tutorial_combined_view, name='tutorial_create'),
    path('tutorial/<int:pk>/', tutorial_combined_view, name='tutorial_update'),
    path('swarm_agents/', swarm_agents_views.swarm_agents, name='swarm_agents'),
    path('report_form/', report_form, name='scientist_report_form'),
    path('submit-disease-info/', submit_disease_info, name='submit_disease_info'),
    path('submit-paper-info/', submit_paper_info, name='submit_paper_info'),
    path('submit-dataset-info/', submit_dataset_info, name='submit_dataset_info'),
    path('search_agents/', search_agents_views.search_view, name='search_agents'),
    path('results/<int:query_id>/', search_agents_views.results_view, name='search_results'),
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)