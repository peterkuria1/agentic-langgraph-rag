


(base) ➜  local-rag pyenv shell 3.11.9

# create virtual env
(base) ➜  local-rag python3 -m venv .venv
# activate virtual environment
(base) ➜  local-rag source .venv/bin/activate
# win: \Scripts\activate

python3 -m pip install streamlit

streamlit run main.py

# deactivate