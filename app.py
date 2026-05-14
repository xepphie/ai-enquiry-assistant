import streamlit as st
from ai_handler import check_enquiry

st.title("AI Client Enquiry Assistant")

enquiry = st.text_area("Paste client enquiry here.")

routing_map = {
    "New Client": "Client Onboarding",
    "Support Request": "Support Team",
    "Complaint": "Support Team",
    "General Question": "Support Team",
    "Billing Issue": "Finance Team",
    "Maintenance Request": "Maintenance Team",
    "Needs Clarification": "Support Team",
    "Error": "IT Team"
}

if st.button("Check"):

    result = check_enquiry(enquiry)

    st.subheader("Classification")
    st.write(result["classification"])

    st.subheader("Confidence")
    st.progress(result["confidence"] / 100)

    st.subheader("Recommended Action")
    st.write(result["action"])

    st.subheader("Suggested Response")
    st.write(result["response"])

    assigned_team = routing_map.get(result["classification"])
    st.subheader("Assigned Team")
    st.write(assigned_team)