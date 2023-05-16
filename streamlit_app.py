import streamlit as st
import os
import openai
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# Set OpenAI API key as environment variable
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Instantiate the LLM model
llm = OpenAI(temperature=0)

# Split text
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(txt)

# Create multiple documents
docs = [Document(page_content=t) for t in texts[:3]]

# Text summarization
chain = load_summarize_chain(llm, chain_type="map_reduce")
chain.run(docs)

st.title('Text Summarization with Langchain')
txt = st.text_area('Enter your text', '')
