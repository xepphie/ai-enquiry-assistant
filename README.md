# ai-enquiry-assistant

An AI-powered assistant designed to deal with and process incoming client enquiries more efficiently for a property management company.

This prototype uses Gemini 2.5 Flash model to classify client enquiries, estimate confidence levels, recommend actions, and generate a professional draft response for staff review.

---

# Streamlit Live Demo

```text
https://ai-enquiry-assistant-2verzmbktdaahqy6h4kxnx.streamlit.app/
```

---

# Features

## AI Enquiry Analysis

The application uses Google's Gemini API to analyse incoming client enquiries and automatically:

- Classify the enquiry type
- Estimate confidence score
- Detect urgency level
- Recommend next actions
- Generate professional draft responses

## Supported Enquiry Categories

- New Client
- Support Request
- Complaint
- Billing Issue
- Maintenance Request
- General Question
- Needs Clarification

## Automation Potential Features

- Potential CRM or email automation integration
- Classify enquiry by urgency and task queue
- Improved routing to appropriate teams
- Enquiry or conversation history with the assistant

## Prompt Engineering Design

The application uses structured prompting to ensure reliable AI outputs.

The AI is instructed to:

- Return only JSON
- Follow a strict response schema
- Avoid markdown formatting
- Provide deterministic structured outputs

Example schema:

```json
{
  "classification": "",
  "confidence": 0,
  "action": "",
  "response": ""
}
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/xepphie/ai-enquiry-assistant.git
cd ai-strata-enquiry-assistant
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Alternatively, for Streamlit Cloud deployment, configure the key using Streamlit Secrets.

---

## 4. Run the Application

```bash
streamlit run app.py
```

---

# Design Decisions

## Why Streamlit?

Streamlit was chosen because it allows me to prototype and deploy light apps with a friendly UI so I can focus more on the functionality.

## Why Gemini?

Gemini provides a free tier of usage with strong performance for small tasks like these.
