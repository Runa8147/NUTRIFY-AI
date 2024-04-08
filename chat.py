import os

import streamlit as st
from time import sleep


import google.generativeai as gen_ai
# Load environment variables


# Configure Streamlit page settings
st.set_page_config(
    page_title="Nutrify chatbot powered by gemini pro",
    page_icon=":brain:", 
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = "AIzaSyAZ35ZoRYAcU-bNLBTHQvEJjSnD9HP8CbY"
# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.0-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title(" Nutrify AI")

# Add small text below the header
st.markdown("Made by  [404 Found](https://404foundxnutrifyai.blogspot.com/)")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask ✨Nutrify AI about your health or nutrition...")
if user_prompt:
  # Add user's message to chat
  st.chat_message("user").markdown(user_prompt)

  # Send prompt with user query
  gemini_response = st.session_state.chat_session.send_message(f"Based on a healthy diet, {user_prompt}")

  # Alternative approach: Analyze keywords in response (not perfect)
  if any(keyword in gemini_response.text.lower() for keyword in ["nutrition", "health", "diet", "exercise"]):
    st.chat_message("assistant").markdown(gemini_response.text)
    like, unlike, save = st.columns(3)  # Add a new column for save button
    with like:
      if st.button(" Like"):
        st.success("Thanks for the feedback!")
    with unlike:
      if st.button(" Unlike"):
        st.warning("I apologize if the information wasn't helpful. I am still under development and learning to focus on providing the best nutritional and health guidance.")
        sleep(8)  # Optional: Display warning for a duration
    with save:
      if st.button(" Save Response"):
        # Download response logic
        response_text = gemini_response.text
        st.download_button(label="Download Response", data=response_text.encode('utf-8'), file_name="nutrify_ai_response.txt", mime="text/plain")
  else:
    st.chat_message("assistant").markdown("It seems your question might be outside my area of expertise. Please rephrase focusing on nutrition or health.")
