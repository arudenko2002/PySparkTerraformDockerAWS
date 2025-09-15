# train_and_save.py
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
import os

# Load California housing dataset
california = fetch_california_housing(as_frame=True)
X = california.data
y = california.target

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train random forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save as MLflow model
out_dir = "model"
os.makedirs(out_dir, exist_ok=True)
mlflow.sklearn.save_model(sk_model=model, path=out_dir)

print("Model saved to", out_dir)
print("Feature names:", list(X.columns))
