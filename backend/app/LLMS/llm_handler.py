import os
import psutil
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.config import MODEL_PATH, HUGGINGFACE_TOKEN, MAX_NEW_TOKENS, TEMPERATURE, TOP_K, TOP_P, NUM_BEAMS, NO_REPEAT_NGRAM_SIZE

# Function to print memory usage
def print_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    memory_usage_in_gb = memory_info.rss / (1024 ** 3)
    print(f"Current memory usage: {memory_usage_in_gb:.2f} GB")

# Set device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Clear GPU memory
if torch.cuda.is_available():
    torch.cuda.empty_cache()

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, token=HUGGINGFACE_TOKEN)

# Load model with memory optimizations
try:
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, 
        token=HUGGINGFACE_TOKEN, 
        torch_dtype=torch.float16  # Use mixed precision to save memory
    ).to(device)
except torch.cuda.OutOfMemoryError:
    print("GPU ran out of memory. Falling back to CPU.")
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, token=HUGGINGFACE_TOKEN).to("cpu")

# Check and set padding token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Print memory usage
print_memory_usage()

# Function to generate response
def process_with_llama(input_text: str):
    print(f"Processing input: {input_text}")
    
    # Move inputs to the same device as the model
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    inputs = inputs.to(model.device)  # Ensure inputs are on the same device as the model
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            top_k=TOP_K,
            top_p=TOP_P,
            num_beams=NUM_BEAMS,
            do_sample=True,
            no_repeat_ngram_size=NO_REPEAT_NGRAM_SIZE,
            early_stopping=True
        )
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print_memory_usage()
    return generated_text


# Test the function
if __name__ == "__main__":
  """   input_text = "Explain the importance of GPUs in AI."
    response = process_with_llama(input_text)
    print("Generated Text:", response) """
