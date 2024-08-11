import requests
import base64
import json
from django.conf import settings
from .Standard_responses import Farmer_response

def analyze_image(image_path: str) -> str:
    standard_response = Farmer_response

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
                            "text": """Analyze this image and provide a detailed report covering the following aspects related to plant health and field conditions:
                            Plant Disease Analysis
                                Disease Name: The scientific and common names of the plant disease.
                                Affected Plant: The specific plant species or variety affected by the disease.
                                Description: A concise description of the disease, including its cause (e.g., fungal, bacterial, viral).
                                Diagnosis Method: Step-by-step methods for diagnosing the disease, including any necessary tools, tests, or observations.
                                Symptoms: Comprehensive details on the symptoms exhibited by the plant, including visual indicators (e.g., leaf spots, wilting, discoloration) and any physiological changes.
                                Management Tips: Practical and effective management strategies, including cultural practices, chemical treatments, and organic solutions.
                                Prevention Strategies: Recommendations for preventing the disease, such as crop rotation, resistant plant varieties, and sanitation practices.
                                Additional Notes: Any extra information that might be helpful, such as regional considerations, lifecycle of the pathogen, or potential impact on yield.
                            Soil and Field Conditions
                                Soil Type: Description of the soil type (e.g., sandy, clay, loamy) visible in the image.
                                Soil Health: Indicators of soil health, including any signs of erosion, compaction, or nutrient deficiencies.
                                Moisture Levels: Assessment of soil moisture levels (e.g., dry, moist, waterlogged) based on visible evidence.
                                Soil pH: If possible, an estimation or indication of soil pH based on the appearance of plants and soil.
                                Nutrient Status: Observations on any visible signs of nutrient imbalances or deficiencies, such as chlorosis or stunting.
                                Field Conditions: Overall field conditions including drainage, topography, and any observable issues like pest infestations or weed growth.
                                Recommendations for Improvement: Suggestions for improving soil health and field conditions, such as soil amendments, irrigation practices, and field management techniques.
                            Format the response as a JSON object."""
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