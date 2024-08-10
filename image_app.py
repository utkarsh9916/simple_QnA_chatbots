# from dotenv import load_dotenv
# load_dotenv()  ## loading all the enviroment variables
# from PIL import Image

# import streamlit as st
# import os   
# import google.generativeai as genai


# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# #  functions to load gemini pro model and get responses

# model=genai.GenerativeModel("gemini-vision-pro")
# def get_gemini_response(input,image):
#     if input!="":
#         response=model.generate_content([input,image])
#     else:
#         response=model.generate_content(image)
#     return response.text


# # initialize our streamlit app

# st.set_page_config(page_title="Sawal-Jawab 2.0")
# st.header("Gemini LLM Application")

# input=st.text_input("Input:", key="Input")

# uploaded_file= st.file_uploader("Choose_an_image.......",type=["jpg","jpeg","png"])
# image = None
# if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image,caption="Uploaded Image", use_column_width=True)

# submit= st.button("Tell me about the image ")


# # when submit is clicked
# if submit:
#     response=get_gemini_response(input,image)
#     st.subheader("The Response is ")
#     st.write(response)


from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

from PIL import Image
import streamlit as st
import os   
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image=None):
    if input_text and image:
        response = model.generate_content([input_text, image])
    elif input_text:
        response = model.generate_content(input_text)
    elif image:
        response = model.generate_content(image)
    else:
        return "No input or image provided"
    
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Sawal-Jawab 2.0")
st.header("Gemini LLM Application")

input_text = st.text_input("Input:", key="Input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me about the image")

# When submit is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("The Response is")
    st.write(response)
