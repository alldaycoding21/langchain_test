# # ✅ Dockerfile
# FROM python:3.10-slim

# WORKDIR /app

# COPY . .

# RUN pip install --upgrade pip \
#  && pip install -r requirements.txt

# EXPOSE 8501
# CMD ["streamlit", "run", "streamlit_app.py"]

FROM python:3.10-slim

WORKDIR /app

# 캐시 최적화: 먼저 requirements 복사
COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt \
 && rm -rf /root/.cache/pip

# 이후 코드 복사
COPY . .

# Streamlit 포트 (기본 8501)
EXPOSE 8501

# 명시적으로 실행 설정
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
