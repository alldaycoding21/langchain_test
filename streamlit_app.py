import streamlit as st
from chains.qa_chain import get_qa_chain

st.set_page_config(page_title="📄 문서 기반 GPT 챗봇")
st.title("🧠 문서 기반 Q&A (로컬 Ollama)")

qa_chain = get_qa_chain()
query = st.text_input("❓ 질문을 입력하세요:")

if query:
    with st.spinner("⏳ 답변 생성 중..."):
        result = qa_chain.invoke(query)  # ← invoke()로 바꾸고 전체 결과 받기

        st.markdown("### 📝 답변")
        st.write(result["result"])

        st.markdown("### 📚 출처")
        for doc in result["source_documents"]:
            st.write("🔹", doc.metadata.get("source", "알 수 없음"))
