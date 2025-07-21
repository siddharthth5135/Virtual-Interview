import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Print the models you can use
for model in genai.list_models():
    print(model.name)
