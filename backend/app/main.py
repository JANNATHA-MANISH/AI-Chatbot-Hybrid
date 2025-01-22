from fastapi import FastAPI, HTTPException
from app.schemas import TextInput, TextOutput, ErrorResponse
from app.pipeline import process_pipeline
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:5500",  # Allow requests from frontend running on port 5500
    "http://127.0.0.1:5500",  # Optional: to handle requests from 127.0.0.1
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/process_text", response_model=TextOutput, responses={400: {"model": ErrorResponse}})
async def process_text(input_data: TextInput):
    try:
        # Process the text using the selected model (Gemini, Llama, or ChatGPT)
        result = process_pipeline(input_data.input_text, input_data.model_name)
        return TextOutput(processed_text=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
