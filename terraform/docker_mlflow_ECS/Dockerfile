# Use slim python
FROM python:3.11-slim

# Create app dir
WORKDIR /app

# Install build deps for some packages if required
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements, install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model
COPY mlflow_api.py /app/mlflow_api.py
COPY model /app/model

# Expose port
ENV PORT=8080
ENV MODEL_PATH=/app/model

# Use uvicorn/gunicorn in production: uvicorn workers are simple — we'll use gunicorn + uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "mlflow_api:app", "-b", "0.0.0.0:8080", "--workers", "2"]