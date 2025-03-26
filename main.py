# from loaders.document_loader import load_documents
# from splitters.text_splitter import split_documents
# from embeddings.embedder import create_vector_store
# from chains.qa_chain import get_qa_chain
# from utils.helpers import print_sources

# def initialize_vector_db():
#     docs = load_documents()
#     chunks = split_documents(docs)
#     create_vector_store(chunks)
#     print("✅ 문서 임베딩 완료!")

# def ask_question():
#     chain = get_qa_chain()
#     query = input("❓ 질문: ")
#     while query:
#         result = chain(query)
#         print_sources(result)
#         query = input("\n❓ 다음 질문 (엔터시 종료): ")

# if __name__ == "__main__":
#     initialize_vector_db()
#     ask_question()

from loaders.document_loader import load_documents
from splitters.text_splitter import split_documents
from embeddings.embedder import create_vector_store
from chains.qa_chain import get_qa_chain

def initialize_vector_db():
    docs = load_documents()
    print(f"📄 불러온 문서 수: {len(docs)}")

    chunks = split_documents(docs)
    print(f"🧩 쪼갠 문서 청크 수: {len(chunks)}")

    create_vector_store(chunks)
    print("✅ 문서 임베딩 완료!")


def ask_question():
    qa = get_qa_chain()
    print("💬 질문을 입력하세요 (종료하려면 Enter):")
    while True:
        query = input("❓ ")
        if not query:
            break
        result = qa(query)
        print("\n📝 답변:\n", result["result"])
        print("\n📚 출처:")
        for doc in result["source_documents"]:
            print(" -", doc.metadata.get("source", "알 수 없음"))

if __name__ == "__main__":
    initialize_vector_db()
    ask_question()
