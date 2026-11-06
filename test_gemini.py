import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check whether the key exists
if not api_key:
    raise ValueError("Gemini API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Gemini client created successfully!")