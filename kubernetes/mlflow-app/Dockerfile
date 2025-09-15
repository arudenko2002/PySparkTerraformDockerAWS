FROM python:3.9-slim

# Install netstat and other tools

RUN apt-get update && apt-get install -y net-tools curl && apt-get clean

RUN pip install --no-cache-dir mlflow[extras] scikit-learn pandas

COPY iris_model /opt/ml/model

ENV MLFLOW_MODEL_SERVE_PORT=1234

EXPOSE 1234

ENTRYPOINT ["mlflow", "models", "serve", "-m", "/opt/ml/model", "-h", "0.0.0.0", "-p", "1234", "--no-conda"]