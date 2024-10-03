
# Local Agentic RAG wit Ollama, streamlit

I have a basic demo for using Llama 3.2 large language model using Retrieval Augument Generation, RAG to retrieve insights from documents embedded. I will be making use of Langgraph and Llama 3.1/3.2 LLM with  Streamlit in building this multi-agentic chatbot.

# Prerequisites

## LLM - using Ollama to fetch the models


```
curl -fsSL https://ollama.com/install.sh | sh
```

# Download the Llama LLM using Ollama
```
ollama run llama3.2:3b # 3b parameters

ollama run llama3.1 # 8B parameters

ollama run llama3.1:70b # 70b
```

(base) ➜  local-rag pyenv shell 3.11.9

# create virtual env
(base) ➜  local-rag python3 -m venv .venv
# activate virtual environment
(base) ➜  local-rag source .venv/bin/activate
# win: \Scripts\activate

```bash
python3 -m pip install streamlit

streamlit run main.py

```

# Open another terminal activate virtual env and lets develop

<!--
# deactivate -->


# to run the app on docker

```bash
cd app/backend
docker compose up -d
```

## to delete the containers

```bash
docker compose down
```