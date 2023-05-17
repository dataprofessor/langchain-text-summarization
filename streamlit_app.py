import streamlit as st
import os
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

with st.sidebar:
  # Check if OpenAI API key is in secrets
  if 'OPENAI_API_KEY' in st.secrets:
    st.success('Key is provided!', icon='🔑')
    os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
  # If API key is not in secrets, ask user to enter key
  else:
    st.error('Please enter your API key!', icon='⚠️')
    api_key = st.text_input('Enter OpenAI API key:', type='password')
    os.environ['OPENAI_API_KEY'] = api_key

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

# Form to accept user's text input for summarization
st.title('🦜🔗 Text Summarization App')
with st.form("summarize_form"):
  txt_input = st.text_area('Enter your text', '', height=200)
  submitted = st.form_submit_button("Submit")
  if submitted:
    summarize(txt_input)
