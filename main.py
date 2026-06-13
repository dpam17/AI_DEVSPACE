import os
# System module to interact with the operating system
from dotenv import load_dotenv
# Library to read .env files

# Load the variables from the .env file into system memory
load_dotenv()

# Retrieve the API key from system memory
api_key = os.getenv("OPENAI_API_KEY")

# Check if the key was loaded successfully
if not api_key:

# Stop the program if the key is missing
 raise ValueError("API key not found! Please check your .env file.")

# Print a success message without exposing the actual secret key
print("API key loaded successfully!")
# FILE: main.py