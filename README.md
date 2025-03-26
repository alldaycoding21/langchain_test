# 🧠 LangChain RAG 기반 문서 Q&A 시스템

GPT와 LangChain을 활용해 **사내 문서 기반 질문/답변 시스템**을 구축하는 오픈소스 프로젝트입니다.  
로컬에 저장된 텍스트 문서를 벡터화하고, GPT를 통해 자연어 질의에 답변합니다.

---

## 📌 주요 기능

- ✅ 문서 업로드 및 자동 임베딩
- ✅ Chroma 벡터 DB 기반 의미 검색
- ✅ OpenAI GPT 모델을 활용한 답변 생성
- ✅ 출처 문서 표시 기능
- ✅ 확장 가능한 폴더 구조 기반 설계
- ✅ API 또는 웹 서버로 확장 가능

---

## 🧱 프로젝트 구조

\`\`\`
langchain-project/
├── main.py
├── config/
├── data/raw_docs/
├── loaders/
├── splitters/
├── embeddings/
├── chains/
├── memory/
├── utils/
├── vector_store/chroma/
├── notebooks/
└── requirements.txt
\`\`\`

---

## ⚙️ 설치 방법

\`\`\`bash
git clone https://github.com/your-username/langchain-project.git
cd langchain-project
pip install -r requirements.txt
\`\`\`

\`.env\` 파일 생성:

\`\`\`
OPENAI_API_KEY=sk-xxxxxxx
\`\`\`

---

## 🚀 실행 방법

\`\`\`bash
python main.py
\`\`\`

1. \`data/raw_docs/\`에 문서(txt) 업로드  
2. 실행 시 문서 → Chunk → 임베딩 → 저장  
3. 질문 입력하면 GPT가 답변 + 출처 제공

---

## 🧪 예시

\`\`\`txt
❓ 질문: 환불은 며칠 이내 가능한가요?

📝 답변:
제품 수령일로부터 7일 이내에 환불이 가능합니다.

📚 출처:
 - refund_policy.txt
\`\`\`

---

## 🧠 기술 스택

| 항목 | 기술 |
|------|------|
| LLM | OpenAI GPT-3.5 / GPT-4 |
| Embedding | OpenAI text-embedding-3-small |
| Vector DB | Chroma (로컬) |
| Framework | LangChain |
| 문서 로더 | langchain.document_loaders |
| Chunking | CharacterTextSplitter |

---

## 🔧 확장 아이디어

- ✅ FastAPI 서버화 → REST API 제공
- ✅ Streamlit UI 챗봇
- ✅ PDF, DOCX, CSV 등 포맷 확장
- ✅ 로컬 모델 (Mistral, Ollama 등) 연결
- ✅ 사용자 인증 / 세션별 메모리

---

## 📄 라이선스

MIT License

---

## 🙌 크레딧

Made with ❤️ by [Your Name]  
Based on OpenAI, LangChain, and Chroma open-source tools.




---개발 내용---
1. 문서 저장 (data/raw_docs/)
2. main.py 실행
   ⤷ 문서 로드 → chunk 나누기 → 벡터화 → 저장
3. 사용자 질문 입력
   ⤷ 관련 문서 검색 → GPT 응답 생성 → 출력 + 출처


📁 폴더 구조 (LangChain + RAG 기반 기준)

langchain_test/
│
├── main.py                     # 메인 실행 파일
├── requirements.txt            # 필요한 패키지 목록
│
├── config/
│   └── settings.py             # API 키, 모델 설정, 경로 등 config
│
├── data/
│   └── raw_docs/               # 원본 문서들 (pdf, txt, md 등)
│
├── loaders/
│   └── document_loader.py      # 문서 로딩 로직
│
├── splitters/
│   └── text_splitter.py        # 문서 chunking 로직
│
├── embeddings/
│   └── embedder.py             # Embedding & 벡터 DB 처리 (예: Chroma)
│
├── chains/
│   ├── qa_chain.py             # Retrieval QA 체인 정의
│   └── chat_chain.py           # Conversational Chain (optional)
│
├── memory/
│   └── memory_config.py        # 메모리 설정 (대화형 컨텍스트 유지)
│
├── utils/
│   └── helpers.py              # 유틸 함수들 (예: 캐싱, 프린터 등)
│
├── api/
│   └── app.py                  # FastAPI or Flask 백엔드 서버 (optional)
│
├── vector_store/
│   └── chroma/                 # Chroma 벡터 DB 저장 폴더 (persisted DB)
│
└── notebooks/
    └── playground.ipynb        # 테스트용 Jupyter notebook


📌 각 폴더 역할 설명
폴더/파일	역할
main.py	프로그램 진입점 (CLI or 테스트 실행)
config/	API Key, 경로, 모델 이름 등 환경 변수 분리
data/	문서 원본 저장
loaders/	다양한 포맷 문서를 LangChain 형식으로 변환
splitters/	문서를 token 단위로 chunking
embeddings/	embedding 생성 및 vector DB 관리 (저장/로드)
chains/	LangChain의 핵심 chain 정의 (QA, 대화형 등)
memory/	사용자 질문/답변 기록 유지 설정
api/	FastAPI 등을 이용해 REST API 서버 구성
vector_store/	Chroma 등의 저장된 DB 경로 설정
notebooks/	실험/테스트/디버깅용 노트북


🧪 개발 플로우 예시
data/raw_docs/에 문서 저장

loaders/에서 문서 로드

splitters/로 chunk 나누기

embeddings/로 벡터화 + Chroma 저장

chains/qa_chain.py에서 검색 기반 QA 시스템 구성

main.py or api/app.py로 실행


✅ 추가 팁
.env 파일에 API 키, 디렉토리 경로 설정 → config/settings.py에서 로딩

scripts/ 폴더 만들어서 임시 테스트용 스크립트 관리도 좋아요

logs/, tests/ 폴더도 실제 서비스 만들 때 추가 가능

