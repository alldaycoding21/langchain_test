import os
from dotenv import load_dotenv

load_dotenv()

PERSIST_DIRECTORY = "vector_store/chroma"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
# LOCAL_MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
LOCAL_MODEL_NAME = "google/gemma-3-4b-it"