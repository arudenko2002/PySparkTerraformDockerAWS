# app.py
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import os

MODEL_PATH = os.getenv("MODEL_PATH", "model")  # path inside container

app = FastAPI(title="California Housing RF Model API")

# California housing dataset features
FEATURES = [
    "MedInc",     # Median income in block group
    "HouseAge",   # Median house age in block group
    "AveRooms",   # Average rooms per household
    "AveBedrms",  # Average bedrooms per household
    "Population", # Block group population
    "AveOccup",   # Average household occupancy
    "Latitude",   # Block group latitude
    "Longitude"   # Block group longitude
]

class PredictRequest(BaseModel):
    data: List[dict]  # list of feature dicts

class PredictResponse(BaseModel):
    predictions: List[float]

# Load MLflow model once
model = mlflow.pyfunc.load_model(MODEL_PATH)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    # Convert request to DataFrame and validate features
    df = pd.DataFrame(req.data)

    missing_cols = [f for f in FEATURES if f not in df.columns]
    if missing_cols:
        return {"error": f"Missing features: {missing_cols}"}

    preds = model.predict(df[FEATURES])
    return {"predictions": [float(p) for p in preds]}