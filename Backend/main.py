from flask import Flask, request
from flask_cors import CORS
import google.generativeai as genaiz  # Correct import
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the API
genaiz.configure(api_key=GOOGLE_API_KEY)  # Use the correct alias

# Initialize the Generative Model with an available model (updated from "models/gemini-pro")
# model = genaiz.GenerativeModel(model_name="models/gemini-1.5-pro")
model = genaiz.GenerativeModel(model_name="models/gemini-2.0-flash")
chat = model.start_chat(history=[])

# Initialize Flask app
app = Flask(__name__)
cors = CORS(app, resources={r"/chat/*": {"origins": "*"}})  # Explicitly allow all origins for chat routes
app.config['CORS_HEADERS'] = 'Content-Type'

chat_name = "Jonathan"
field_name = "PHP Developer"

# Initial interview message
init_message = (
    f"*You are an HR manager skilled at evaluating employees and asking interview questions. "
    f"First, introduce yourself as {chat_name}, a Virtual HR Manager, conducting an interview "
    f"for a {field_name} job. Ask the user for an introduction. Keep responses short and avoid using system text.*"
)

@app.route("/chat/get-init-message", methods=['GET'])
def chat_get_init_message():
    chat.history.clear()  # Clear chat history
    return chat.send_message(init_message).text

@app.route("/chat/send-message", methods=['POST'])
def chat_send_message():
    message = request.form['message']
    ended = False

    # Adjust message based on interview progress
    if len(chat.history) < 5:
        message += " *Give short feedback and ask the next interview question.*"
    elif len(chat.history) < 13:
        message += " *If it was a technical question, evaluate the answer and ask another technical question.*"
    else:
        message += " *Interview has ended. Send a closing message and state whether the candidate is accepted or rejected for the next round.*"
        ended = True

    # Send response message and status
    return {
        "message": chat.send_message(message).text,
        "ended": ended,
    }

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Ensure the server is accessible
