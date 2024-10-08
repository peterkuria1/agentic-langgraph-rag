import logging
from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)
from langchain_core.documents import Document

# Creating an object
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Load Data
def load_data(file_type: str, file_loc: str) -> List[Document]:
    try:
        """Please load data into a list of Documents
        Args:
            file_type: the type of file to load
        Returns:    list of Documents
        """
        if file_type == "PDF":
            loader = PyPDFLoader(file_loc)
            data = loader.load()

        elif file_type == "Text":
            loader = TextLoader(r"{}".format(file_loc))
            data = loader.load()

        elif file_type == "DOCX":
            loader = Docx2txtLoader(file_loc)
            data = loader.load()

        elif file_type == "Markdown":
            loader = UnstructuredMarkdownLoader(file_loc)
            data = loader.load()
        logger.info("Loaded the Document")

        return data

    except Exception as e:
        logger.error(f"An error occurred in load_data: {str(e)}")
        raise SystemExit(f"Exiting due to the error: {str(e)}")


# Prepare Chunks
def prepare_chunk(data: list) -> List[Document]:
    """Prepare documents into chunks
    Args:
        data: list of Documents
    Returns: list of Chunks
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=600, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
        )
        documents = text_splitter.split_documents(data)
        logger.info(f"Splitted the document into {len(documents)} chunks")

        return documents, len(documents)

    except Exception as e:
        logger.error(f"An error occurred in prepare_chunk: {str(e)}")
        raise SystemExit(f"Exiting due to the error: {str(e)}")