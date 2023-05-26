from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define some responses
greetings = ["Hi there!", "Hello!", "Greetings!"]
questions = ["How can I assist you?", "What can I do for you?", "How may I help you?"]
goodbyes = ["Goodbye!", "Have a nice day!", "Bye!"]

# Define some functions to handle incoming messages
def handle_greeting():
    return random.choice(greetings)

def handle_question():
    return random.choice(questions)

def handle_goodbye():
    return random.choice(goodbyes)

# Define the main route for the chatbot
@app.route("/", methods=["POST"])
def chatbot():
    data = request.get_json()

    # Extract the user's message
    message = data["message"]

    # Determine the appropriate response based on the message
    if "hi" in message.lower() or "hello" in message.lower():
        response = handle_greeting()
    elif "help" in message.lower() or "assistance" in message.lower():
        response = handle_question()
    elif "bye" in message.lower() or "goodbye" in message.lower():
        response = handle_goodbye()
    else:
        response = "I'm sorry, I don't understand. Could you please rephrase?"

    # Construct and return the response
    response_data = {
        "message": response
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
