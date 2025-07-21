🚀 Virtual HR Manager – Backend (Flask) with venv Setup

Overview
This project is the backend (Flask API) for the Virtual HR Manager, built in Python. It features a simple chat-based interview system powered by Google Generative AI. All environment and dependency management is handled through a project-local virtual environment (venv), ensuring clean and reproducible installs.

Features
Flask-based REST API for chat sessions ([GET]/chat/get-init-message, [POST]/chat/send-message).
CORS support to allow connections from frontend or other domains.
Google Generative AI model integration for real-time conversational logic.
.env management for secure API keys and secrets.

Backend Setup: Complete Guide (with venv)

1. Prerequisites
Python 3.8+
Internet connection (for installing packages)
Access to a Google Generative AI API key

2. Quickstart Steps

a. Clone the Repository
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name/Backend

b. Create and Activate a Virtual Environment (venv)
On Windows:
python -m venv venv
venv\Scripts\activate
On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
You should see (venv) in your command prompt, indicating the virtual environment is active.

c. Install Dependencies
pip install -r requirements.txt
# If requirements.txt is missing, install manually:
pip install flask flask-cors python-dotenv google-generativeai

d. Environment Variables

e. Create a .env file in your backend directory:
   GOOGLE_API_KEY=your-google-api-key-here

f. Run the Flask Server
   python main.py
   The server will start on http://0.0.0.0:5000. You can test using tools like Postman or directly from your frontend.



Notes & Recommendations
Always activate your venv before running or installing anything!
Do not commit the venv folder or .env file to git (add them to .gitignore).
After running, deactivate your venv any time with the deactivate command.
To upgrade dependencies, run pip install --upgrade ... inside your virtual environment.
