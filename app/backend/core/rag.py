import logging
from io import BytesIO
from typing import List

import streamlit as st
from langchain_core.documents import Document

from core.loader import load_data, prepare_chunk
from core.retriever import run_llm
from core.utils import check_valid_file
from core.vector_stores import create_vector_stores
# Creating an object
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def loader(file: BytesIO, file_loc: str):
    try:
        file_type = check_valid_file(file)
        data = load_data(file_type=file_type, file_loc=file_loc)
        documents, chunks = prepare_chunk(data)
        if chunks == 0:
            logger.error("Error in preparing chunks")
            documents = None

        return documents

    except Exception as e:
        st.info(f"An error occurred in loader: {str(e)}")
        raise SystemExit(f"Sorry Error: exiting now.: {str(e)}")


def vector_stores(documents: List[Document]):
    try:
        vs_conn = create_vector_stores(documents)

        return vs_conn

    except Exception as e:
        st.info(f"An error occurred in vector stores: {str(e)}")
        raise SystemExit(f"Sorry Error: exiting now.: {str(e)}")


def retrieval(
    model_name: str, user_question: str, session_id: str, vstore_connection=None
):
    try:
        response = run_llm(
            model_name=model_name,
            user_question=user_question,
            vstore_connection=vstore_connection,
            session_id=session_id,
        )
        return response.content

    except Exception as e:
        st.info(f"An error occurred in retrieval: {str(e)}")
        raise SystemExit(f"Sorry Error: exiting now.: {str(e)}")