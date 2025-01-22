# Import necessary functions for each model
from app.LLMS.gemini_api import process_with_gemini
from app.LLMS.openai_api import process_with_chatgpt
from app.LLMS.gorq_ai import process_with_gorq  # Assuming you have a gorq_api module
from app.LLMS.deepseek_AI import process_with_deepseek  # Assuming you have a deepseek_api module
# from app.LLMS.llm_handler import process_with_llama  # Uncomment if using Llama

def process_pipeline(input_text: str, model_name: str) -> str:
    """
    Decides which model to use based on the 'model_name' parameter.

    Args:
    - input_text (str): The input text to be processed.
    - model_name (str): The name of the model to use (e.g., 'gemini', 'chatgpt', 'gorq', 'deepseek').

    Returns:
    - str: The processed response from the selected model.

    Raises:
    - ValueError: If the model_name is not supported.
    """
    if model_name == 'gemini':
        return process_with_gemini(input_text)  # Process with Gemini API
    elif model_name == 'chatgpt':
        return process_with_chatgpt(input_text)  # Process with ChatGPT (OpenAI API)
    elif model_name == 'groq':
        return process_with_gorq(input_text)  # Process with Gorq API
    elif model_name == 'deepseek':
        return process_with_deepseek(input_text)  # Process with Deepseek API
    # elif model_name == 'llama':
    #     return process_with_llama(input_text)  # Process with local Llama model
    else:
        raise ValueError(f"Unsupported model: {model_name}")