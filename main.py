from loaders.document_loader import load_documents
from splitters.text_splitter import split_documents
from embeddings.embedder import create_vector_store
from chains.qa_chain import get_qa_chain
from utils.helpers import print_sources

def initialize_vector_db():
    docs = load_documents()
    chunks = split_documents(docs)
    create_vector_store(chunks)
    print("✅ 문서 임베딩 완료!")

def ask_question():
    chain = get_qa_chain()
    query = input("❓ 질문: ")
    while query:
        result = chain(query)
        print_sources(result)
        query = input("\n❓ 다음 질문 (엔터시 종료): ")

if __name__ == "__main__":
    initialize_vector_db()
    ask_question()
