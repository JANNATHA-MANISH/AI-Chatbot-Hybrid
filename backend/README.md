
---

# AI HYBRIDFLOW API: Local and API-Based Language Models

This repository demonstrates the integration of a **local LLM (LLaMA)** and an **API-based LLM (Google Gemini)** in a unified **AI Hybrid Data Processing Pipeline**. Instructions are provided to clone, set up, and run both methods for text processing tasks.

## **Project Overview**

- **Local LLM (LLaMA)**: A lightweight language model that runs locally, requiring minimal resources. It's ideal for smaller text processing tasks and can be deployed on local hardware with lower memory consumption.
  
- **API-Based LLM (Google Gemini)**: A powerful cloud-based language model from Google, capable of handling more complex text processing tasks. It requires an API key and an internet connection.

---

## **Getting Started**

Follow the steps below to clone the repository, install dependencies, and run the model locally or using the Google Gemini API.

### **1. Clone the Repository**

To begin, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/AIHYBRIDFLOW-API.git
cd AIHYBRIDFLOW-API
```

### **2. Set Up the Environment**

Create a virtual environment and install the required dependencies.

#### For Windows:

```bash
# Create a virtual environment
python -m venv llmenv

# Activate the environment
llmenv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

#### For macOS/Linux:

```bash
# Create a virtual environment
python3 -m venv llmenv

# Activate the environment
source llmenv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

### **3. Requirements**

The repository contains the necessary requirements in `requirements.txt`. Some critical dependencies include:

- `transformers`: For loading pre-trained models such as LLaMA and Google Gemini.
- `fastapi`: For creating API endpoints to interact with the models.
- `uvicorn`: A fast ASGI server to run the FastAPI app.
- `google-generativeai`: For interacting with Google's Gemini API.
- `torch`: For running models locally (if using LLaMA).

### **4. Set Up API for Google Gemini**

To use the Google Gemini API, you need an API key. Follow these steps:

- Go to the **Google Cloud Console** and create a new project.
- Enable the **Generative AI API**.
- Create API credentials (API Key).
- Set the API key in the `.env` file under `GEMINI_API_KEY`.

### **5. Run the Local LLM (LLaMA)**

To run the LLaMA model locally, use **Uvicorn** to run the FastAPI app:

```bash
# Run the FastAPI app with Uvicorn
uvicorn app.main:app --reload
```

- **Access Local Documentation**: After running the server, open your browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation.
- You can now send a request to the API by hitting the `/process_text` endpoint.

### **6. Run the API-Based LLM (Google Gemini)**

To use the **Google Gemini** API, ensure that you have set up the API key in the `.env` file:

```env
GEMINI_API_KEY=your_google_api_key_here
```

- **Run the FastAPI app** (similar to LLaMA, but using API access):

```bash
uvicorn app.main:app --reload
```

- **Access Local Documentation**: After running the server, open your browser and navigate to `http://127.0.0.1:8000/docs`.
  - Use the `/process_text` endpoint to send a request to the Google Gemini API.

### **7. Test the Endpoints**

Once the server is running:

- Open your browser at `http://127.0.0.1:8000/docs`.
- Use the API documentation to send a POST request to `/process_text` with the following JSON body:

```json
{
  "input_text": "What is the capital of France?",
  "use_gemini": false
}
```

- The `use_gemini` field determines whether the text is processed by the local model (LLaMA) or the Google Gemini API.
  - Set `use_gemini = true` to use the Google Gemini API.

### **8. Comparing Local LLaMA vs API-Based Gemini**

- **Local LLaMA**:
  - Lightweight and runs directly on your machine.
  - Suitable for basic text generation tasks.
  - **Memory usage** is low (about 2GB RAM).
  - **Free** to use as it runs locally.

- **Google Gemini API**:
  - Requires an **API key** and internet connection.
  - Can handle more complex tasks and larger data inputs.
  - **Paid**: Google's pricing applies based on usage.
  - **Memory usage** depends on the complexity of the task but offloads the work to Google's cloud.

---

## **Troubleshooting**

- **Error: “Model not found”**: Ensure the model path is correct in the `.env` file or check that you have the proper API key for Google Gemini.
- **Error: “ModuleNotFoundError”**: Ensure you have installed all dependencies by running `pip install -r requirements.txt`.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Screenshots**

Here are the sample outputs you can expect from the system:

**LLaMA (Local Model) Output:**

- Input: `What is the meaning of life?`
- Output: `The meaning of life is subjective and varies for each individual.`

**Google Gemini (API-Based Model) Output:**

- Input: `What is the capital of France?`
- Output: `The capital of France is Paris.`

---

**Image Prompt for README:**

You can use this prompt for generating images:
- "Illustration of a machine learning model with a local LLM and API model comparison, showing server architecture with an API call to Google Gemini."

---

### **Next Steps**

Feel free to explore the API and experiment with different input texts. This setup allows you to test local language models and cloud-based models like Google Gemini seamlessly!

---

This updated `README.md` now includes clear instructions to run the FastAPI app with the `uvicorn app.main:app --reload` command for both local and API-based LLM tasks.
=======
# AI-HYBRIDFLOW-API
AIHYBRIDFLOW-API is a flexible data processing pipeline that integrates both external APIs (like OpenAI or Gemini) and local AI models (such as LLaMA). The pipeline bridges the gap between cloud-based and local AI processing, offering robust, hybrid flow capabilities for structured data output, error handling, and seamless integration.
>>>>>>> f23453d92a80daf7b88c149a923e5b885eedc963
=======
# AI-HYBRIDFLOW-API
AIHYBRIDFLOW-API is a flexible data processing pipeline that integrates both external APIs (like OpenAI or Gemini) and local AI models (such as LLaMA). The pipeline bridges the gap between cloud-based and local AI processing, offering robust, hybrid flow capabilities for structured data output, error handling, and seamless integration.
>>>>>>> f23453d92a80daf7b88c149a923e5b885eedc963
