@app.post("/chat")
def chat(request:ChatRequest):
    response = ollama.chat(
        model="gemma2n:e2b",
        messages=[
            {
                "role":"user",
                "content":request.message
            }
        ]
    )
    return response["messages"]["content"]