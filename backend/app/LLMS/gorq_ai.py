import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=groq_api_key)

def process_with_gorq(input_text: str) -> str:
    """
    Function to send input text to the Groq API and get the processed response.

    Args:
    - input_text (str): The input text to be processed by Groq API.

    Returns:
    - str: The processed response from the Groq API.
    """
    try:
        # Send the input text to the Groq API
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ],
            model="mixtral-8x7b-32768",  # Example model
            temperature=0.7,
            max_tokens=1000
        )
        
        # Return the response text from Groq
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error occurred while processing with Groq: {e}")
        return "Sorry, there was an error processing your request."