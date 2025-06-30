import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load from .env

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_gemini_response(prompt):
   try:
        response = model.generate_content(prompt)
        return response.text
   except Exception as e:
        return f"Error: {str(e)}"
   
   
   
   # we need to install some pakages to deal with api of ai
   #   1) pip install generativeai
   #   2)pip install dotenv   --- environment where api keys are stored safely