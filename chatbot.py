import random

# Predefined responses with keywords
responses = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "answers": [
            "Hello there! How can I help you?",
            "Hi! What’s up?",
            "Hey! Need any assistance?"
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how's it going", "how do you do"],
        "answers": [
            "I'm functioning perfectly, thank you!",
            "Doing great! How about you?",
            "I’m just a program, but I’m feeling awesome!"
        ]
    },
    "name": {
        "keywords": ["your name", "who are you", "what's your name"],
        "answers": [
            "I’m ChatBot, your friendly assistant.",
            "They call me ChatBot.",
            "I'm your rule-based chatbot friend!"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "answers": [
            "Goodbye! Have a great day!",
            "See you later!",
            "Bye! Come back soon."
        ]
    }
}

print("Hello! I am ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    found_match = False
    for intent, data in responses.items():
        if any(keyword in user_input for keyword in data["keywords"]):
            print("Bot:", random.choice(data["answers"]))
            found_match = True
            if intent == "goodbye":
                exit()
            break

    if not found_match:
        print("Bot: Hmm... I’m not sure I understand. Could you rephrase?")
