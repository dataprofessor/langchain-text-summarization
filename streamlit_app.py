import streamlit as st
import os
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


if os.getenv('OPENAI_API_KEY') is not None:
  # Set OpenAI API key as environment variable
  #os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
  os.environ['OPENAI_API_KEY'] = st.text_input('Enter OpenAI API key:', type='password')
else:
  st.success('Key is provided!', icon='🔑')

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
