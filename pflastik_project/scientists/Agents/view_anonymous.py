import requests
import base64
import json
from django.conf import settings
from .Standard_responses import Anonymous_response

def analyze_image(image_path: str):
    standard_response = Anonymous_response
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
                            "text": "Analyze this image and provide a detailed report on any plant diseases you can identify. Include the disease name, affected plant, description, diagnosis method, symptoms, management tips, and any additional notes. Format the response as a JSON object."
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
        response.raise_for_status()
        response_data = response.json()
        
        # Parse the OpenAI response content as JSON
        openai_response = json.loads(response_data['choices'][0]['message']['content'])
        return openai_response
    except json.JSONDecodeError:
        print("Failed to parse OpenAI response as JSON. Returning standard response.")
        return standard_response
    except Exception as e:
        print(f"Error during image analysis: {str(e)}")
        return standard_response