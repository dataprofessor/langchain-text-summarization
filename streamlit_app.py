import streamlit as st
import os
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# Check if OpenAI API key is in secrets
if 'OPENAI_API_KEY' in st.secrets:
  st.success('Key is provided!', icon='🔑')
  os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
else:
  st.error('Please enter your API key!', icon='⚠️')
  api_key = st.text_input('Enter OpenAI API key:', type='password')
  os.environ['OPENAI_API_KEY'] = api_key

#api_key = st.text_input('Enter OpenAI API key:', type='password')
#if api_key:
#  os.environ['OPENAI_API_KEY'] = api_key  
  
#if os.getenv('OPENAI_API_KEY'):
  # Set OpenAI API key as environment variable
  #os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
  #os.environ['OPENAI_API_KEY'] = st.text_input('Enter OpenAI API key:', type='password')
  #st.success('Key is provided!', icon='🔑')
#else:
  #st.error('Please enter API key!', icon='⚠️')


def summarize(txt):
  # Instantiate the LLM model
  llm = OpenAI(temperature=0)
  # Split text
  text_splitter = CharacterTextSplitter()
  texts = text_splitter.split_text(txt)
  # Create multiple documents
  docs = [Document(page_content=t) for t in texts[:3]]
  # Text summarization
  chain = load_summarize_chain(llm, chain_type="map_reduce")
  return st.info(chain.run(docs))

st.title('🦜🔗 Text Summarization App')

with st.form("summarize_form"):
  txt_input = st.text_area('Enter your text', '', height=200)
  submitted = st.form_submit_button("Submit")
  if submitted:
    summarize(txt_input)
