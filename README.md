# 🧠 LangChain + Ollama 기반 로컬 문서 Q&A 시스템

로컬 LLM인 **Ollama**와 **LangChain**, **Chroma**, **Streamlit**, **FastAPI**를 이용해
완전한 오프라인 문서 기반 Q&A 시스템을 구축합니다.

---

## 🚀 주요 기능

- ✅ 로컬 LLM (`gemma3`, `mistral` 등) 사용 – Ollama 기반
- ✅ HuggingFace Embedding 모델로 문서 임베딩
- ✅ Chroma 벡터DB로 유사도 기반 문서 검색
- ✅ LangChain RAG 체인 구성 (`RetrievalQA`)
- ✅ CLI, Streamlit, FastAPI 3가지 인터페이스 제공
- ✅ `launch.py` 및 `docker-compose`로 통합 실행 지원

---

## 📂 프로젝트 구조

```
langchain_test/
├── main.py                     # CLI 기반 문서 Q&A
├── launch.py                  # 실행 메뉴 (CLI / UI / API)
├── streamlit_app.py           # Streamlit UI 앱
├── api/
│   └── app.py                 # FastAPI 서버
├── chains/
│   └── qa_chain.py            # RetrievalQA 체인 구성
├── llm/
│   └── local_model.py         # Ollama 모델 로딩
├── loaders/
│   └── document_loader.py     # 텍스트 문서 로더
├── splitters/
│   └── text_splitter.py       # 문서 chunk 처리
├── embeddings/
│   └── embedder.py            # HuggingFace 임베딩
├── vector_store/              # Chroma 벡터 저장소
├── data/raw_docs/             # 사용자 문서 입력 경로
├── Dockerfile                 # Streamlit 실행용
├── Dockerfile.api             # FastAPI 실행용 (선택)
├── docker-compose.yml         # 통합 실행 스크립트
└── requirements.txt
```

---

## ✅ 실행 방법

### 🧪 1. 가상환경 설치 및 라이브러리 설치

```bash
python -m venv venv_langchain
source venv_langchain/bin/activate
pip install -r requirements.txt
```

### 🔍 2. Ollama 모델 실행 (별도 터미널)
```bash
ollama pull gemma3
ollama run gemma3
```

### 🔧 3. CLI 실행 (문서 임베딩 + 질문 응답)
```bash
python main.py
```

### 🌐 4. Streamlit 실행
```bash
streamlit run streamlit_app.py
```

### 🚀 5. FastAPI 실행
```bash
uvicorn api.app:app --reload
```

---

## ⚡ 통합 실행 (추천)

### ✅ `launch.py`
```bash
python launch.py
```
- CLI / Streamlit / FastAPI / Ollama 실행 선택 가능

### ✅ Docker Compose 실행
```bash
docker-compose up --build
```
- Streamlit + FastAPI 자동 실행 (Ollama는 호스트에서 수동 실행 필요)

---

## 🔧 환경 설정 (.env 예시)
```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
PERSIST_DIRECTORY=vector_store/chroma
```

---

## 📊 향후 확장 가능 기능

- 📁 PDF, CSV, DOCX 등 다양한 문서 포맷 로딩
- 🔐 사용자 인증 / 토큰 제한 / 사용자별 로그 저장
- 🔁 Hybrid Search + Reranker (ex. BGE + cosine rerank)
- 🌍 LangChain Agents + Tools (계산기, Web 검색 등)
- 🧠 LangGraph 멀티스텝 Reasoning

---

## ✅ 모델 추천 (Ollama 기준)

| 모델 | 설명 |
|-------|------|
| `gemma3` | 가볍고 빠른 Q&A 모델 |
| `mistral` | 일반적인 질문 응답에 적합 |
| `llama2` | 대화형 응답에 적합 |
| `phi`     | 컴팩트하고 빠름 |

---

## ✅ 기술 스택

- **LangChain**: 체인 구성 / 프롬프트 관리 / 벡터 검색
- **Ollama**: 로컬 LLM (gemma3, mistral 등)
- **Chroma**: 벡터 저장소
- **HuggingFace**: 문서 임베딩 모델
- **Streamlit**: 웹 UI
- **FastAPI**: API 서버
- **Docker Compose**: 통합 실행 및 배포

---

💡 *이 프로젝트는 완전한 오프라인 RAG 문서봇 구축의 실전 예제입니다.*

필요 시 `llama.cpp`, `LangGraph`, `Web UI`, `Supabase 연동`, `GPT-4 Turbo` 대응도 가능!
