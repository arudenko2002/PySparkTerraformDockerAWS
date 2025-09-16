from mlflow.tracking import MlflowClient

client = MlflowClient()
versions = client.get_latest_versions("IrisClassifier")

for v in versions:
    print(f"Version: {v.version}, Run ID: {v.run_id}, Source: {v.source}")