# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
# from config.settings import PERSIST_DIRECTORY, EMBEDDING_MODEL

# def create_vector_store(docs):
#     embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
#     vectordb = Chroma.from_documents(
#         documents=docs,
#         embedding=embeddings,
#         persist_directory=PERSIST_DIRECTORY
#     )
#     vectordb.persist()
#     return vectordb

# def load_vector_store():
#     embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
#     return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)

# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config.settings import PERSIST_DIRECTORY, EMBEDDING_MODEL

def create_vector_store(docs):
    if not docs:
        print("❌ 문서가 없습니다. 벡터 저장소를 생성하지 않습니다.")
        return

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )
    vectordb.persist()
    print("✅ 벡터 저장소 생성 완료!")

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embeddings)
