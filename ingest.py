import os
import json
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters  import RecursiveCharacterTextSplitter

from config import FAISS_DIR, METADATA_FILE, EMBEDDING_MODEL
from utils.loaders import load_document


embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


def load_metadata():
    if not os.path.exists(METADATA_FILE):
        return {"processed_files": []}

    with open(METADATA_FILE, "r") as f:
        return json.load(f)



def save_metadata(metadata):
    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f, indent=2)



def load_or_create_vectorstore():
    if os.path.exists(os.path.join(FAISS_DIR, "index.faiss")):
        return FAISS.load_local(
            FAISS_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return None



def ingest_file(file_path):
    metadata = load_metadata()
    filename = os.path.basename(file_path)

    if filename in metadata["processed_files"]:
        return "Already processed"

    docs = load_document(file_path)
    chunks = splitter.split_documents(docs)

    vectorstore = load_or_create_vectorstore()

    if vectorstore:
        vectorstore.add_documents(chunks)
    else:
        vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(FAISS_DIR)

    metadata["processed_files"].append(filename)
    save_metadata(metadata)

    return "Ingestion complete"