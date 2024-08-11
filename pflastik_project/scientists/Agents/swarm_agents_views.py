
from django.shortcuts import render

from django.http import HttpResponse
# Agents are maintaied by the hive from external system you can find some S A claesses in AI_tools 
def swarm_agents(request):
   context = {
        'fields_monitored': 5,
        'active_drones': 12,
        'total_flight_hours': 1250,
        'data_collected': '8.5 TB',
        'drone_image_url': 'https://enterprise.dronenerds.com/wp-content/uploads/2023/09/eBee-X-Camera.png',
        'drone_specs': {
            'number_of_units': 5,
            'flight_time': 'Up to 90 minutes',
            'weight': '1.6 kg (3.5 lbs)',
            'max_coverage': '500 ha (1,235 ac) at 120 m (400 ft)',
            'sensors': ['RGB', 'Multispectral', 'Thermal']
        },
        'soil_health': {
            'pH': '6.8 (Slightly acidic)',
            'organic_matter': '3.5%',
            'nitrogen': '45 ppm',
            'phosphorus': '35 ppm',
            'potassium': '180 ppm'
        },
        'crop_health': {
            'NDVI': '0.75 (Healthy vegetation)',
            'leaf_area_index': '3.8',
            'chlorophyll_content': '45 SPAD',
            'crop_water_stress_index': '0.3'
        },
        'pest_and_disease': {
            'detected': ['Aphids', 'Powdery Mildew'],
            'detection_rate': '5% of field',
            'treatment_recommended': 'Yes'
        },
        'crop_rows': ["50", "100", "150", "200", "250", "300", "350", "400", "450", "500", "550"]
    }
   return render(request, 'swarm_agents.html', context)
