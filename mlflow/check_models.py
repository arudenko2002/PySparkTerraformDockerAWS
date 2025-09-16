from mlflow.tracking import MlflowClient
client = MlflowClient()
models = client.search_registered_models()
print([m.name for m in models])  # Should include 'IrisClassifier'

versions = client.get_latest_versions("IrisClassifier")

for v in versions:
    print(f"Version: {v.version}, Run ID: {v.run_id}, Source: {v.source}")