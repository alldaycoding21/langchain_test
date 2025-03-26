from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from embeddings.embedder import load_vector_store

def get_qa_chain():
    vectordb = load_vector_store()
    retriever = vectordb.as_retriever()
    llm = OpenAI(temperature=0)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return chain
