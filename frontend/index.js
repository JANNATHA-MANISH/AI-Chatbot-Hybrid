// Get references to elements
const chatbotConversation = document.getElementById('chatbot-conversation');
const userInputElement = document.getElementById('user-input');
const loadingIndicator = document.getElementById('loading-indicator');
const modelDropdown = document.getElementById('model-dropdown'); // Dropdown element
const buttons = document.querySelectorAll('.model-btn'); // Buttons

// Handle user input submission
document.addEventListener('submit', (e) => {
    e.preventDefault();
    const userInput = userInputElement.value;
    
    // Display the user's message in the conversation
    addMessageToChat(userInput, true);
    userInputElement.value = '';

    // Show loading indicator
    loadingIndicator.style.display = 'block';

    // Send the input to the backend (port 8000)
    sendToBackend(userInput);
});

// Function to add a message to the chat
function addMessageToChat(message, isUser) {
    const chatContainer = document.getElementById('chatbot-conversation');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('speech', isUser ? 'speech-human' : 'speech-ai');
    messageDiv.textContent = message;
    chatContainer.appendChild(messageDiv);

    // Scroll to the bottom of the chat container
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Function to send user input to the backend
function sendToBackend(inputText) {
    const selectedModel = getSelectedModel(); // Get the current selected model
    
    // Prepare the data to send to the backend
    const requestData = {
        input_text: inputText,
        model_name: selectedModel
    };

    // Send POST request to the backend (localhost:8000)
    fetch('http://localhost:8000/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to get a valid response from the server');
        }
        return response.json();
    })
    .then(data => {
        addMessageToChat(data.processed_text, false); // Display AI's response
    })
    .catch(error => {
        console.error('Error with request to backend:', error);
        addMessageToChat("Sorry, there was an error processing your request.", false);
    })
    .finally(() => {
        // Hide loading indicator
        loadingIndicator.style.display = 'none';
    });
}

// Get the selected model based on the active button or dropdown
function getSelectedModel() {
    if (window.innerWidth <= 480) {
        // Mobile: Get selected model from dropdown
        return modelDropdown.value;
    } else {
        // Desktop: Get selected model from buttons
        const selectedButton = [...buttons].find(button => button.classList.contains('selected'));
        return selectedButton ? selectedButton.id.replace('-btn', '') : 'gemini'; // Default to 'gemini' if no button is selected
    }
}

// Event listener for model selection buttons (desktop)
buttons.forEach(button => {
    button.addEventListener('click', () => {
        setActiveButton(button.id.replace('-btn', ''));
        console.log('Selected Model:', button.id.replace('-btn', '').toUpperCase());
    });
});

// Event listener for model dropdown (mobile)
modelDropdown.addEventListener('change', () => {
    console.log('Selected Model:', modelDropdown.value.toUpperCase());
});

// Helper function to set active button (desktop)
function setActiveButton(selectedModel) {
    buttons.forEach(button => {
        button.classList.remove('selected');
    });

    const selectedButton = document.getElementById(`${selectedModel}-btn`);
    selectedButton.classList.add('selected');
}