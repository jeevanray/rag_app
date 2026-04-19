# LangGraph + FAISS + Groq + Streamlit RAG

> A lightweight, restart-safe local RAG application built with **LangGraph**, **FAISS**, **Groq**, and **Streamlit**.
>
> Upload documents → Persist embeddings locally → Ask questions → Get context-aware answers.

---

## Overview

This project is designed for practical GenAI learning and production-style implementation.

Instead of recreating embeddings every time the app restarts, the system stores the FAISS index locally and only processes new files.

This makes it:

- restart-safe
- token efficient
- memory efficient
- simple to scale later
- suitable for real-world internal knowledge assistants

---

## Features

### Document Upload Support

Upload and process:

- PDF files
- CSV files
- TXT files

---

### Persistent Local Vector Store

- FAISS index stored locally
- embeddings created only once
- avoids repeated embedding cost
- incremental ingestion support

---

### LLM Integration

Powered by:

- Groq API
- Llama 3.1 8B Instant

Fast inference with low cost for learning and development.

---

### Stateful Workflow

Built using:

- LangGraph

Supports structured retrieval → generation workflow instead of sending full documents every time.

---

### Streamlit UI

Simple UI for:

- uploading documents
- asking questions
- testing RAG quickly

---

## Project Structure

```text
rag_app/
│
├── app.py
├── config.py
├── ingest.py
├── rag_chain.py
├── requirements.txt
│
├── data/
│   ├── uploads/
│   ├── faiss_index/
│   └── metadata.json
│
└── utils/
    └── loaders.py
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| Workflow | LangGraph |
| Vector Store | FAISS |
| Embeddings | HuggingFace |
| LLM | Groq |
| Model | Llama 3.1 8B Instant |
| File Parsing | PyPDF + CSV Loader + Text Loader |

---

## Setup Using UV

### Create Project

```bash
mkdir rag_app
cd rag_app

uv init
uv venv
```

---

### Activate Environment

### Linux / Mac

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
uv add streamlit \
langchain \
langgraph \
langchain-community \
langchain-openai \
langchain-huggingface \
langchain-text-splitters \
faiss-cpu \
pypdf \
pandas \
python-dotenv \
sentence-transformers
```

---

## Environment Variable

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Small Test File

Use this first before large PDFs:

```text
Trino is a distributed SQL query engine used for big data analytics.

FAISS is a vector database library used for similarity search and retrieval.

LangGraph helps build stateful workflows for LLM applications.

Groq provides very fast inference for open-source LLMs like Llama models.

RAG stands for Retrieval-Augmented Generation.
```

Test Question:

```text
What is FAISS used for?
```

---

## Why This Architecture

Most beginner RAG projects fail because they:

- recreate embeddings every run
- waste tokens by sending full documents
- have no persistence
- are difficult to scale

This project avoids that.

It follows a cleaner engineering approach:

### Retrieve only what is needed

instead of

### Sending everything to the LLM

This reduces:

- token cost
- latency
- infrastructure waste

---

## Future Improvements

Phase 2 upgrades:

- SQLite metadata tracking
- document delete/update support
- source citations
- hybrid search
- compression retriever
- audit logging
- background ingestion workers
- Oracle / Mongo integration
- enterprise GraphRAG

---

## Git Ignore

```gitignore
.venv/
__pycache__/
*.pyc
.env
data/faiss_index/
data/uploads/
data/metadata.json
.streamlit/
```

---

## Author

Built for practical GenAI engineering, RAG systems, and production-style LLM workflows.

Focused on real-world implementation over tutorial-style demos.

---

## License

MIT License

