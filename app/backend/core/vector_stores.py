import logging

import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant

# Creating an object
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Local Embedding
# from llama_index.core import settings
# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# from llama_index.llms.openai import OpenAI

# import os
# os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI API KEY>"

# embed_model = NomicEmbedding(
#     api_key=nomic_api_key,
#     dimensionality=128,
#     model_name="nomic-embed-text-v1.5",
# )

# llm = OpenAI(model="gpt-3.5-turbo")
# # print(embed_model['usage'])
# # embeddings = np.array(embed_model["data"])
# # print(embeddings.shape)

# settings.llm = llm
# settings.embed_model = embed_model


# Vector stores
def create_vector_stores(documents: list):
    try:
        logger.info("****Local Embedding is in progress, Please wait...****")
        embeddings = HuggingFaceEmbeddings()

        logger.info("****Loading to Vectorstore, Please wait...****")
        logger.info(f"Adding {len(documents)} to Qdrant Local")
        qdrant = Qdrant.from_documents(
            documents,
            embeddings,
            url="http://localhost:6333",
            collection_name="my_documents",
            force_recreate=True,
        )
        logger.info("****Loading to Vectorstore, Done!****")

        return qdrant

    except Exception as e:
        logger.error(f"An error occurred in create_vector_stores: {str(e)}")
        st.info(f"An error occurred in create_vector_stores: {str(e)}")
        raise SystemExit(f"Exiting due to the error: {str(e)}")