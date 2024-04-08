import streamlit as st

st.title("Nutrify ai")
st.subheader("Nutrify: Your AI-Powered Partner for a Healthier You")
st.image("logo.png",width=100)
st.write("""
  Nutrify is an innovative chatbot designed to make achieving your nutritional goals easier and more accessible. 
  Powered by Gemini, a cutting-edge large language model from Google AI, Nutrify provides personalized guidance 
  and information to help you navigate the world of nutrition.
  """)

st.page_link("home.py", label="Home", icon="🏠")
st.page_link("chat.py", label="Chat", icon="1️⃣")
st.page_link("about.py", label="About", icon="2️⃣")
st.page_link("https://404foundxnutrifyai.blogspot.com/", label="Blog", icon="🌎")


