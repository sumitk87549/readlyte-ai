from fastapi import FastAPI
import ollama
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message:str

@app.post("/chat")
async def chat(request: ChatRequest):

    response = ollama.chat(
        model='gemma3n:e2b',
        messages=[
            {
                "role":"user",
                "content":request.message
            }
        ]
    )

    return {
        "response": response["messages"]["content"]
    }

@app.get("/")
def hello_world():
    return "Hello World"