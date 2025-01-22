from pydantic import BaseModel

# Schema for input text and model selection
class TextInput(BaseModel):
    input_text: str  # The raw input text
    model_name: str  # Model selection: 'gemini', 'llama', 'chatgpt'

# Schema for output (response) from the model (Gemini, Llama, or ChatGPT)
class TextOutput(BaseModel):
    processed_text: str  # The output generated from the selected model

# Schema for error responses
class ErrorResponse(BaseModel):
    detail: str  # Description of the error
