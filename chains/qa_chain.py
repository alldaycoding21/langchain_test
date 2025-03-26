# from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
# from embeddings.embedder import load_vector_store

# def get_qa_chain():
#     vectordb = load_vector_store()
#     retriever = vectordb.as_retriever()
#     llm = OpenAI(temperature=0)

#     chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         return_source_documents=True
#     )
#     return chain

# ✅ chains/qa_chain.py (Ollama용 LLM 사용)
from langchain.chains import RetrievalQA
from llm.local_model import load_local_llm
from embeddings.embedder import load_vector_store

def get_qa_chain():
    llm = load_local_llm()
    vectordb = load_vector_store()
    retriever = vectordb.as_retriever()

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return chain
