from fastapi import FastAPI
from pydantic import BaseModel
from chains.qa_chain import get_qa_chain

app = FastAPI()
qa_chain = get_qa_chain()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(q: Query):
    result = qa_chain.run(q.question)
    return {"answer": result}
