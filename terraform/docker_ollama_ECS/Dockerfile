# Stage 1: Base environment
FROM python:3.11-slim AS base

# Install dependencies for Ollama + FastAPI
RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Install Ollama CLI
#RUN curl -fsSL https://ollama.com/download/ollama-linux-amd64 -o /usr/local/bin/ollama && chmod +x /usr/local/bin/ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set up workdir
WORKDIR /app

# Copy FastAPI app
COPY ollama_api.py /app/

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn requests

# Copy models (blobs + manifests) into the image
# Make sure your build context includes .ollama/models
COPY .ollama /root/.ollama

# Expose ports:
# 11434 = Ollama backend
# 8080  = FastAPI wrapper
EXPOSE 8080 11434

# Stage 2: Run both Ollama and FastAPI
# CMD ["sh", "-c", "ollama serve & uvicorn ollama_api:app --host 0.0.0.0 --port 8080 --timeout-keep-alive 4000"]
# Stage 2: Run both Ollama and FastAPI
CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull llama3 && uvicorn ollama_api:app --host 0.0.0.0 --port 8080 --timeout-keep-alive 4000"]
