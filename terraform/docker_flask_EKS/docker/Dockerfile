FROM python:3.11-slim

# Install dependencies for pyodbc
RUN apt-get update && \
    apt-get install -y \
    unixodbc \
    unixodbc-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY .. .

# Expose port
EXPOSE 5000

# Run Flask
CMD ["python", "flask_app.py"]