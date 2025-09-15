# Dockerfile
FROM python:3.9

# Install system dependencies and Microsoft ODBC Driver
RUN apt-get update && apt-get install -y \
    gnupg2 \
    curl \
    gcc \
    g++ \
    unixodbc \
    unixodbc-dev \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .. .

CMD ["python", "flask_app.py"]