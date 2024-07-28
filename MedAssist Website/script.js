let preferredLanguage = "en"; // Default language is English
let preferredResponseType = "text"; // Default response type is text

// Function to handle sending message
function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;

    displayMessage(userInput, "user");

    // If language preference is not set, ask for language preference
    if (!window.askedLanguage) {
        window.askedLanguage = true;
        displayMessage("Please select your preferred language using the dropdown menu.", "bot");
        return;
    }

    // If response type preference is not set, ask for response type preference
    if (!window.askedResponseType) {
        window.askedResponseType = true;
        displayMessage("Do you prefer text or audio responses?", "bot");
        return;
    }

    // If language preference is set, process user input based on preferences
    if (preferredLanguage === "en") {
        processUserInput(userInput);
    } else {
        translateToPreferredLanguage(userInput);
    }

    document.getElementById("user-input").value = "";
}

// Function to handle displaying messages
function displayMessage(message, sender) {
    const chatMessages = document.getElementById("chat-messages");
    const messageElement = document.createElement("div");
    messageElement.textContent = message;
    messageElement.classList.add("message");

    if (sender === "user") {
        messageElement.classList.add("user-message");
    } else {
        messageElement.classList.add("bot-message");

        if (preferredResponseType === "audio") {
            speak(message);
        }
    }

    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    if (sender === "bot" && preferredResponseType === "text") {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

// Function to process user input based on preferences
function processUserInput(input) {
    const resultDisease = identifyDisease(input);
    displayMessage("Based on your symptoms, you may have " + resultDisease, "bot");

    const med = resultDisease;
    const medToTake = medicationsData[med] ? medicationsData[med][0] : null;

    if (medToTake) {
        displayMessage("In this disease, you can take this medicine: " + medToTake, "bot");
    } else {
        displayMessage("You should consult a doctor", "bot");
    }
}

// Function to handle language selection
function setLanguage(language) {
    preferredLanguage = language;
    displayMessage("You have selected " + language + " language.", "bot");
}

// Function to handle response type selection
function setResponseType(responseType) {
    preferredResponseType = responseType;
    displayMessage("You have selected " + responseType + " responses.", "bot");
}

// Function to speak text
function speak(text) {
    const speech = new SpeechSynthesisUtterance();
    speech.text = text;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}

// Function to translate user input to preferred language
function translateToPreferredLanguage(userInput) {
    googleTranslateElementInit = function() {
        new google.translate.TranslateElement({
            pageLanguage: 'en', // Source language
            includedLanguages: [preferredLanguage], // Target language
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE
        }, 'google_translate_element');
    };
    displayMessage(userInput, "bot");
}
