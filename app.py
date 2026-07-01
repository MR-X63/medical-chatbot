import streamlit as st
from chatbot import MedicalChatbot
from hospitals import get_hospitals
import re

st.set_page_config(page_title="Medical Chatbot", page_icon="🏥")
st.title("🏥 Medical Chatbot")
st.caption("Describe your symptoms and get possible diagnoses and hospital suggestions.")
st.markdown("Built by **Sayyed Shan**")

# Input API key once and store it
if "bot" not in st.session_state:
    api_key = st.text_input("Enter your Groq API key to start:", type="password")
    if api_key:
        st.session_state.bot = MedicalChatbot(api_key)
        st.session_state.messages = []
        st.rerun()
    st.stop()

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Describe your symptoms...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot reply
    reply = st.session_state.bot.send_message(user_input)

    # Show bot reply
    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Check for specialty and show hospitals
    match = re.search(r"SPECIALTY:\s*(.+)", reply)
    if match:
        specialty = match.group(1).strip()
        city = st.text_input("Enter your city to find nearby hospitals:")
        if city:
            hospitals = get_hospitals(specialty, city)
            if hospitals:
                st.subheader(f"Recommended hospitals for {specialty}:")
                for h in hospitals:
                    st.write(f"- **{h['name']}** ({h['city']}) - {h['phone']}")
            else:
                st.write(f"No hospitals found for {specialty} in {city}.")
