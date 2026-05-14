import google.genai as genai
from dotenv import load_dotenv
import os
import json

from prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def check_enquiry(enquiry):

    prompt = f"""
    {SYSTEM_PROMPT}

    Client Enquiry:
    {enquiry}
    """

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        return json.loads(text)

    except Exception as e:

        return {
            "classification": "Error",
            "confidence": 0,
            "action": "Manual review required",
            "response": f"Processing failed: {str(e)}"
        }
