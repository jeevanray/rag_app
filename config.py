import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

BASE_DIR = "data"
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
FAISS_DIR = os.path.join(BASE_DIR, "faiss_index")
METADATA_FILE = os.path.join(BASE_DIR, "metadata.json")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.1-8b-instant"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(FAISS_DIR, exist_ok=True)