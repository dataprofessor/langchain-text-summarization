import streamlit as st
import os
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

def generate_response(txt):
  # Instantiate the LLM model
  llm = OpenAI(temperature=0)
  # Split text
  text_splitter = CharacterTextSplitter()
  texts = text_splitter.split_text(txt)
  # Create multiple documents
  docs = [Document(page_content=t) for t in texts[:3]]
  # Text summarization
  chain = load_summarize_chain(llm, chain_type='map_reduce')
  return st.info(chain.run(docs))

# Page title
st.set_page_config(page_title='🦜🔗 Ask the Doc App')
st.title('🦜🔗 Text Summarization App')

# Text input
txt_input = st.text_area('Enter your text', '', height=200)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
  openai_api_key = st.text_input('OpenAI API Key', type = 'password')
  #txt_input = st.text_area('Enter your text', '', height=200)
  submitted = st.form_submit_button('Submit')
  if submitted and openai_api_key.startswith('sk-'):
    response = generate_response(txt_input)
    result.append(response)
    del openai_api_key

if len(result):
  st.info(response)
