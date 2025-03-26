from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from config.settings import PERSIST_DIRECTORY, EMBEDDING_MODEL

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )
    vectordb.persist()
    return vectordb

def load_vector_store():
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
