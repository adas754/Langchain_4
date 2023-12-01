from langchain.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


# Fetch the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = OpenAI(model_name="text-davinci-003", temperature=0.5, openai_api_key=openai_api_key)
    response = llm(question)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# Input field for user question
input_question = st.text_input("Input: ", key="input")

# If "Ask the question" button is clicked
if st.button("Ask the question"):
    # Check if the input is not empty
    if input_question:
        response = get_openai_response(input_question)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please enter a question.")
