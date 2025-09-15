import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set tracking URI
mlflow.set_tracking_uri("sqlite:///C:/Users/AlexR/PycharmProjects/pythonProject/mlflow/mlruns.db")

# Set experiment
mlflow.set_experiment("Iris-Experiment")

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Start MLflow run
with mlflow.start_run() as run:
    mlflow.sklearn.log_model(
        clf,
        artifact_path="model",
        input_example=X_test[:1],
        registered_model_name="IrisClassifier"
    )
    mlflow.log_metric("accuracy", clf.score(X_test, y_test))
    print(f"✅ Model logged and registered in run: {run.info.run_id}")
    # saves model locally, no need to do it if the model is logged
    # mlflow.sklearn.save_model(
    #     sk_model=clf,
    #     path="iris_model"
    # )