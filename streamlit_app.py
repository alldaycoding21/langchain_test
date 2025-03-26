# ✅ streamlit_app.py
import streamlit as st
from chains.qa_chain import get_qa_chain

st.set_page_config(page_title="📄 Ollama GPT 문서봇")
st.title("🧠 문서 기반 Q&A (Ollama 모델)")

qa_chain = get_qa_chain()
query = st.text_input("❓ 질문을 입력하세요:")

if query:
    result = qa_chain.run(query)
    st.markdown(f"### 📝 답변:\n{result}")