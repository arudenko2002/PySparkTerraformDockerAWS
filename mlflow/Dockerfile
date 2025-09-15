FROM python:3.9-slim

RUN pip install mlflow[extras] scikit-learn pandas

COPY iris_model /opt/ml/model

EXPOSE 1234

ENTRYPOINT ["mlflow", "models", "serve", "-m", "/opt/ml/model", "-h", "0.0.0.0", "-p", "1234"]