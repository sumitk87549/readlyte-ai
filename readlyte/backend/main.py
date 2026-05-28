from fastapi import FastAPI
import ollama

app = FastAPI()

@app.post("/chat")
async def chat()