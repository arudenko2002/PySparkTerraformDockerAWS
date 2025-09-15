#!/bin/sh
set -e

export OLLAMA_HOST=http://127.0.0.1:11434   # <-- FIX

echo "Starting Ollama daemon..."
ollama serve &
pid=$!

echo "Waiting for Ollama to be ready..."
until curl -s http://127.0.0.1:11434/api/tags >/dev/null 2>&1; do
    echo "Waiting..."
    sleep 2
done

#echo "Pulling model if not present..."
#ollama pull llama3:3b || true

echo "Starting FastAPI..."
exec uvicorn ollama_api:app --host 0.0.0.0 --port 8080