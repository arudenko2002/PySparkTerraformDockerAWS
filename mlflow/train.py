import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)
print("X",X)
print("y",y)
print("types", type(X), type(y))
X_train, X_test, y_train, y_test = train_test_split(X, y)
print("X_train",X_train)
print("y_train",y_train)
print("X_test",X_test)
print("y_test", y_test)

# Start MLflow run
with mlflow.start_run() as run:
    # Hyperparameters
    n_estimators = 100
    max_depth = 3

    # Train model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train)
    # run_id = run.info.run_id
    # mlflow.sklearn.log_model(model, "model")
    # mlflow.register_model(f"runs:/{run.info.run_id}/model", "IrisClassifier")
    preds = model.predict(X_test)
    print("preds",preds)

    # Metrics
    acc = accuracy_score(y_test, preds)
    print("acc",acc)

    # Log parameters, metrics, and model
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

    print(f"Logged with accuracy: {acc:.4f}")
    result = mlflow.register_model("runs:/f2524f7948da4988b5d45d098f8135a4/model", "IrisClassifier")
    # mlflow models serve -m runs:/f2524f7948da4988b5d45d098f8135a4/model -p 1234

    mlflow.sklearn.log_model(model, "model")
    mlflow.register_model(f"runs:/{run.info.run_id}/model", "IrisClassifier")