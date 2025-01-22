import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the DeepSeek API key
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
if not deepseek_api_key:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set.")

# DeepSeek API endpoint
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # Replace with the actual API endpoint

def process_with_deepseek(input_text: str) -> str:
    """
    Function to send input text to the DeepSeek API and get the processed response.

    Args:
    - input_text (str): The input text to be processed by DeepSeek API.

    Returns:
    - str: The processed response from the DeepSeek API.
    """
    try:
        # Prepare the request payload
        payload = {
            "model": "deepseek-v3",  # Replace with the correct model name
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        # Make the API request
        headers = {
            "Authorization": f"Bearer {deepseek_api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)

        # Check for errors in the response
        if response.status_code != 200:
            print(f"DeepSeek API Error: {response.status_code} - {response.text}")
            return "Sorry, there was an error processing your request."

        # Extract and return the response text
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    
    except Exception as e:
        print(f"Error occurred while processing with DeepSeek: {e}")
        return "Sorry, there was an error processing your request."