import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hi!"],
    "how are you?": ["I'm doing well, thanks for asking.", "I'm fine, thanks!", "Not too bad, thanks!"],
    "what's your name?": ["My name is Chatbot.", "I'm Chatbot.", "Call me Chatbot!"],
    "default": ["I'm sorry, I don't understand what you're saying.", "Can you please rephrase that?"]
}

def chat():
    print("Hello, I'm Chatbot! How can I assist you today?")
    while True:
        user_input = input().lower()
        if user_input == "bye":
            print("Goodbye!")
            break
        if user_input in responses:
            bot_response = random.choice(responses[user_input])
        else:
            bot_response = random.choice(responses["default"])
        print(bot_response)

chat()

