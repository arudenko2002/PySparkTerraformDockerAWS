import mlflow
client = mlflow.tracking.MlflowClient()

run = client.get_run("f2524f7948da4988b5d45d098f8135a4")
print(run.info)

with mlflow.start_run() as run:
    # Train model
    mlflow.sklearn.log_model(model, "model")
    mlflow.register_model(f"runs:/{run.info.run_id}/model", "IrisClassifier")