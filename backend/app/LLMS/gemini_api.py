import os
import google.generativeai as genai
from dotenv import load_dotenv  # To load .env file if you're using it

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define the generation configuration for Gemini
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the generative model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start the chat session with Gemini
chat_session = model.start_chat(history=[])

def process_with_gemini(input_text: str) -> str:
    """
    Function to send input text to the Gemini API and get the processed response.

    Args:
    - input_text (str): The input text to be processed by Gemini API.

    Returns:
    - str: The processed response from the Gemini API.
    """
    try:
        # Send the input text to the Gemini API via the chat session
        response = chat_session.send_message(input_text)

        # Return the response text from Gemini
        return response.text
    
    except Exception as e:
        print(f"Error occurred while processing with Gemini: {e}")
        return "Sorry, there was an error processing your request."
