import openai
from app.config import OPENAI_API_KEY

# Configure OpenAI API Key
openai.api_key = OPENAI_API_KEY

def process_with_chatgpt(input_text: str) -> str:
    """
    Function to send input text to the OpenAI ChatGPT API and get the processed response.

    Args:
    - input_text (str): The input text to be processed by ChatGPT API.

    Returns:
    - str: The processed response from ChatGPT.
    """
    try:
        # Make a request to the ChatGPT API using the correct interface
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or another model like gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        # Extract the generated text from the response
        return response['choices'][0]['message']['content']
    
    except Exception as e:
        print(f"Error occurred while processing with ChatGPT: {e}")
        return "Sorry, there was an error processing your request."
