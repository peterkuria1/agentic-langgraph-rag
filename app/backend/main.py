import streamlit as st
import pandas as pd
import numpy as np

import openai
import time
import os

from core.utils import get_session, sidebar
from streamlit.logger import get_logger

from core.retriever import run_llm
from core.loader import load_data, prepare_chunk
from core.rag import loader, vector_stores, retrieval

from core.vector_stores import create_vector_stores

logger = get_logger(__name__)

st.set_page_config(
    page_title="AgenticRAG",
    initial_sidebar_state="expanded",
    menu_items={"About": "# *Agentic Local RAG* with  Gdrants, postgres and Ollama"},
)

st.header("Agentic GraphRAG with Qdrant, Ollama and Postres")

sidebar()

uploaded_file = st.file_uploader("Please upload a file", type=("pdf", "docx", "txt", "md",))


def setup():
    if not uploaded_file:
        st.stop()

    if uploaded_file:
        st.toast("Your file has been uploaded!", icon="✅")
        time.sleep(0.5)

        with open(uploaded_file.name, mode="wb") as w:
            w.write(uploaded_file.getvalue())

        documents = loader(file=uploaded_file, file_loc=uploaded_file.name)
        os.remove(uploaded_file.name)
        if documents is None:
            st.info("No data found, please upload a valid file")
            st.stop()

        elif documents is not None:
            with st.spinner("Please wait for Indexing docs"):
                vs_conn = vector_stores(documents=documents)
                st.toast("File indexing completed", icon="🚀")
                time.sleep(0.5)

    return vs_conn


def welcome_message():
    # Initialize chat history
    st.session_state.messages = [
        {"role": "assistant", "content": "Chat with your document, any question?"}
    ]
    with st.chat_message("assistant"):
        for msg in st.session_state.messages:
            st.markdown(msg["content"])
    # Create session id to store chat history in redis
    st.session_state.session_id = get_session()


if __name__ == "__main__":
    if "messages" not in st.session_state:
        vs_conn = setup()
        welcome_message()
    if prompt := st.chat_input():
        rag_chat(prompt, model="llama3")