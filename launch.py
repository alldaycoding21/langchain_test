# ✅ launch.py - 실행 선택 메뉴
import os
import subprocess

MENU = """
🔰 실행할 항목을 선택하세요:
1. CLI (main.py)
2. Streamlit UI (http://localhost:8501)
3. FastAPI 서버 (http://localhost:8000/docs)
4. Ollama 모델 실행 (gemma3)
5. 전체 자동 실행 (Ollama + Streamlit)
0. 종료
"""

while True:
    print(MENU)
    choice = input("선택 (0~5): ").strip()

    if choice == "1":
        os.system("python main.py")
    elif choice == "2":
        os.system("streamlit run streamlit_app.py")
    elif choice == "3":
        os.system("uvicorn api.app:app --reload")
    elif choice == "4":
        subprocess.Popen(["ollama", "run", "gemma3"])
        print("✅ gemma3 모델 실행 중... 백그라운드에서 동작합니다.")
    elif choice == "5":
        subprocess.Popen(["ollama", "run", "gemma3"])
        subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
        print("✅ Ollama + Streamlit UI 동시 실행 중!")
    elif choice == "0":
        print("👋 종료합니다.")
        break
    else:
        print("❌ 잘못된 선택입니다. 다시 입력해주세요.")
