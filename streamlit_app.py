import streamlit as st
import openai
import os
import requests

# Set OpenAI API key as environment variable
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Initialize session state
if 'txt' not in st.session_state:
    st.session_state['txt'] = ''

    
st.title('Text Summarization with Langchain')

txt = st.text_area('Text to analyze', '')

st.write('Hello world!')
