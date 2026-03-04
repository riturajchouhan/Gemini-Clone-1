import streamlit as st
import google.generativeai as genai

# Yahan apni API Key dalein
api_key = st.secrets["GEMINI_API_KEY"] # Ye line Streamlit se key khud utha legi
genai.configure(api_key=api_key)

# Model ki setting (aap isse 'cool' bana sakte hain)
model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",
    system_instruction="Tum ek friendly aur smart AI clone ho. Tumhara naam 'MyGemini' hai."
)

st.set_page_config(page_title="AI Clone", page_icon="🤖")
st.header("🤖 Mera Apna Gemini Clone")

# Chat memory initialize karna
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Purani chats dikhana
for message in st.session_state.chat_session.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# User ka sawal
user_input = st.chat_input("Mujhse kuch puchiye...")

if user_input:
    # User ka message screen par dikhana
    st.chat_message("user").markdown(user_input)
    
    # Gemini se jawab lena
    response = st.session_state.chat_session.send_message(user_input)
    
    # AI ka jawab dikhana
    with st.chat_message("assistant"):
        st.markdown(response.text)
    