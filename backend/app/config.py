import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Hugging Face API Token and Model Path
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")  # For security, use environment variables
MODEL_PATH = os.getenv("MODEL_PATH", "meta-llama/Llama-3.2-1B")  # Default to Llama if not specified

# Generation parameters
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", 1024))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
TOP_K = int(os.getenv("TOP_K", 40))
TOP_P = float(os.getenv("TOP_P", 0.95))
NUM_BEAMS = int(os.getenv("NUM_BEAMS", 5))
NO_REPEAT_NGRAM_SIZE = int(os.getenv("NO_REPEAT_NGRAM_SIZE", 2))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#OPENAI KEY

# Any other configurations
