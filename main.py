from fastapi import FastAPI
from pydantic import BaseModel
from functions import webOrchestration
from codeCleaner import *
import json

app = FastAPI()

class ReqData(BaseModel):
    prompt: str


@app.get("/")
def read_root():
    return {"message": "Crisp, shits workin"}

@app.post("/get_code")
def create_code(reqData: ReqData):
    prompt = reqData.prompt
    print(prompt)
    output = webOrchestration(prompt = prompt)
    # cleaned_code = clean_code_output(output)
    # formated_code = json.dumps(cleaned_code, indent=2)
    return {"code": output}
    
