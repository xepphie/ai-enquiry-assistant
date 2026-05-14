from google import genai
from dotenv import load_dotenv
import streamlit as st
import json

from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def check_enquiry(enquiry):

    prompt = f"""
    {SYSTEM_PROMPT}

    Client Enquiry:
    {enquiry}
    """

    try:
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)

        text = response.text.strip()

        return json.loads(text)

    except Exception as e:

        return {
            "classification": "Error",
            "confidence": 0,
            "action": "Manual review required",
            "response": f"Processing failed: {str(e)}"
        }