import requests
import base64
import json
from django.conf import settings
from .Standard_responses import Scientist_response

def analyze_image(image_path):
    standard_response = Scientist_response #json.dumps(Scientist_response, indent=2)

    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """
                                Analyze this image and provide a comprehensive scientific report covering the following aspects related to plant health, soil conditions, and biochemical analysis:
                                Plant Disease Analysis
                                    Disease Name: The scientific and common names of the plant disease.
                                    Affected Plant: The specific plant species or variety affected by the disease.
                                    Pathogen Information: Detailed information about the pathogen (e.g., fungal, bacterial, viral), including its scientific classification and life cycle.
                                    Description: An in-depth description of the disease, its etiology, and epidemiology.
                                    Diagnosis Method: Detailed methods for diagnosing the disease, including visual inspections, laboratory tests (e.g., PCR, ELISA), and any required equipment.
                                    Symptoms: Comprehensive details on the symptoms exhibited by the plant, including morphological, physiological, and molecular indicators.
                                    Management Strategies: Advanced management strategies, including integrated pest management (IPM) practices, chemical treatments, biological controls, and genetic resistance.
                                    Prevention Strategies: Detailed recommendations for preventing the disease, including cultural practices, resistant cultivars, and biosecurity measures.
                                    Additional Notes: Any extra information that might be helpful, such as insights into the pathogen's lifecycle, environmental conditions favoring the disease, and potential impacts on crop yield and quality.
                                Plant Information
                                    Plant Biology: Detailed information on the plant's biology, including growth stages, physiological processes, and relevant genetic information.
                                    Chemical Composition: Analysis of the plant's chemical composition, including key metabolites, nutrients, and potential toxins.
                                    Proteins: Information on important proteins within the plant, including their functions and relevance to plant health and disease resistance.
                                    Genetic Markers: Identification of any genetic markers associated with disease resistance or susceptibility.
                                Soil and Field Conditions
                                    Soil Type: Detailed description of the soil type (e.g., sandy, clay, loamy) and its characteristics based on the image.
                                    Soil Health Indicators: Analysis of soil health, including signs of erosion, compaction, organic matter content, and microbial activity.
                                    Moisture Levels: Assessment of soil moisture levels with possible techniques to measure and maintain optimal moisture.
                                    Soil pH: Estimation or measurement of soil pH based on visual clues and potential impact on plant health.
                                    Nutrient Status: Detailed observations on nutrient status, including potential deficiencies or toxicities, supported by visible symptoms and recommended soil tests.
                                    Field Conditions: Comprehensive assessment of field conditions including drainage patterns, topography, pest infestations, and weed growth.
                                    Chemical Analysis: Information on the presence and concentration of relevant chemicals in the soil, including fertilizers, pesticides, and pollutants.
                                    Recommendations for Improvement: Scientific recommendations for improving soil health and field conditions, such as specific soil amendments, irrigation practices, cover cropping, and field management techniques.
                                    Research Insights: Relevant research findings or recent studies that could provide additional context or innovative solutions for the identified issues.
                                Format the response as a JSON object and reference the provided image for accuracy. This detailed scientific analysis will aid in advancing research and practical solutions for plant health, soil management, and overall field optimization.
                                """
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 500
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        response_data = response.json()

        # Attempt to parse the OpenAI response as JSON
        try:
            openai_response = json.loads(response_data['choices'][0]['message']['content'])
            return json.dumps(openai_response, indent=2)
        except json.JSONDecodeError:
            print("Failed to parse OpenAI response as JSON. Returning standard response.")
            return standard_response

    except Exception as e:
        print(f"Error during image analysis: {str(e)}")
        return standard_response