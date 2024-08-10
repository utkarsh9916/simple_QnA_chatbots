from dotenv import load_dotenv
load_dotenv()  ## loading all the enviroment variables

import streamlit as st
import os   
import google.generativeai as genai


genai.configure(api_key=os.getenv("Add your api key"))

#  functions to load gemini pro model and get responses

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(questions):
    response=model.generate_content(questions)
    return response.text


# initialize our streamlit app

st.set_page_config(page_title="Sawal-Jawab")
st.header("Gemini Application")

input=st.text_input("Input:", key="Input")
submit= st.button("Ask the Question")


# when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)
    
