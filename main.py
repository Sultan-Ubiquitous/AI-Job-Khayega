from fastapi import FastAPI
from pydantic import BaseModel
from functions import webOrchestration

app = FastAPI()

class Negro(BaseModel):
    prompt: str


@app.get("/")
def read_root():
    return {"message": "Crisp, shits workin"}

@app.post("/get_code")
def create_code(negro: Negro):
    prompt = negro.prompt
    print(prompt)
    output = webOrchestration(prompt = prompt)
    return output
    
