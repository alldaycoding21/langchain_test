def print_sources(result):
    print("\n📝 답변:")
    print(result["result"])
    print("\n📚 출처:")
    for doc in result["source_documents"]:
        print(" -", doc.metadata.get("source", "알 수 없음"))
