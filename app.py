import os
import streamlit as st

from config import UPLOAD_DIR
from ingest import ingest_file

st.set_page_config(page_title="Local RAG Assistant")

st.title("LangGraph + FAISS + Groq RAG")

st.subheader("Upload Documents")

uploaded_file = st.file_uploader(
    "Upload PDF / CSV / TXT",
    type=["pdf", "csv", "txt"]
)

if uploaded_file:
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    result = ingest_file(save_path)
    st.success(result)

st.divider()

st.subheader("Ask Questions")

question = st.text_input("Enter your question")

if st.button("Ask") and question:
    from rag_chain import ask_question

    answer = ask_question(question)
    st.write(answer)