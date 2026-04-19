from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import FAISS_DIR, EMBEDDING_MODEL, GROQ_API_KEY, LLM_MODEL


class GraphState(TypedDict):
    question: str
    context: str
    answer: str


embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

vectorstore = FAISS.load_local(
    FAISS_DIR,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

llm = ChatOpenAI(
    model=LLM_MODEL,
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY,
    temperature=0,
    max_tokens=500, # type: ignore
)



def retrieve(state: GraphState):
    docs = retriever.invoke(state["question"])
    context = "\n\n".join([doc.page_content for doc in docs])
    return {"context": context}



def generate(state: GraphState):
    prompt = f"""
    Use only the provided context.

    Context:
    {state['context']}

    Question:
    {state['question']}
    """

    response = llm.invoke(prompt)
    return {"answer": response.content}


builder = StateGraph(GraphState)

builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)

builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

app = builder.compile()



def ask_question(question):
    result = app.invoke({"question": question})
    return result["answer"]