from fastapi import FastAPI, HTTPException
import requests
import os
import json

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
if not OLLAMA_HOST.startswith("http://") and not OLLAMA_HOST.startswith("https://"):
    OLLAMA_HOST = f"http://{OLLAMA_HOST}"

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/generate")
def generate(prompt: str):
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={"model": "llama3:latest", "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()

        # Ollama sometimes returns multiple JSON objects separated by newlines
        texts = []
        for line in response.text.splitlines():
            if line.strip():
                try:
                    data = json.loads(line)
                    if "response" in data:
                        texts.append(data["response"])
                except json.JSONDecodeError:
                    continue

        return {"model": "llama3:latest", "output": "".join(texts)}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))