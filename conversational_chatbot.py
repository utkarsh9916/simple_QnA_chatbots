

from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

import google.generativeai as genai

# Configure the generative AI model

genai.configure(api_key=os.getenv("Add your api key"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit
st.set_page_config(page_title="Simple Q&A Bot")
st.header("Apna Bot")

# Initialize session state for chat history if it does not exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Initialize the list

input_text = st.text_input("Input:", key="Input")
submit = st.button("Ask me")

if submit and input_text:
    response = get_gemini_response(input_text)
    
    # Add user query to session chat history
    st.session_state['chat_history'].append(("You", input_text))
    
    st.subheader("The response is")
    
    # Display response chunks and add them to the chat history
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

    st.subheader("The chat history is")

# Display chat history
if 'chat_history' in st.session_state:
    for role, text in st.session_state.chat_history:  # Access with dot notation
        st.write(f"{role}: {text}")
