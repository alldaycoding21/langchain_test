# from langchain.llms import HuggingFacePipeline
# from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
# from config.settings import LOCAL_MODEL_NAME

# def load_local_llm():
#     tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL_NAME)
#     model = AutoModelForCausalLM.from_pretrained(LOCAL_MODEL_NAME, device_map="auto")

#     pipe = pipeline(
#         "text-generation",
#         model=model,
#         tokenizer=tokenizer,
#         max_new_tokens=512,
#         temperature=0.7,
#         do_sample=True,
#         repetition_penalty=1.1
#     )
#     return HuggingFacePipeline(pipeline=pipe)

# ✅ llm/local_model.py (Ollama 연결용)
import os
from langchain_community.llms import Ollama


def load_local_llm():
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    return Ollama(model="gemma3", base_url=base_url)
