import random

import streamlit as st


def check_valid_file(file) -> str:
    """Reads an uploaded file and returns a File object"""
    if file.name.lower().endswith(".docx"):
        return "DOCX"
    elif file.name.lower().endswith(".pdf"):
        return "PDF"
    elif file.name.lower().endswith(".txt"):
        return "Text"
    elif file.name.lower().endswith(".md"):
        return "Markdown"
    else:
        raise NotImplementedError(f"File type {file.name.split('.')[-1]} not supported")


def get_session():
    hash = random.getrandbits(128)

    return str(hash)


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Follow the [prerequisites]()\n"
            "2. Run the LocalRAG app locally using streamlit\n"
            "2. Upload a pdf, docx, txt or md file📄\n"
            "3. Ask a question about the document💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📝This is a self-hosted RAG app using python and Qdrant, python"
        )

        st.markdown("---")