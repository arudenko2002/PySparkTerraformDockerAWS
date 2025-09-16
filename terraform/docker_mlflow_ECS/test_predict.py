import mlflow.pyfunc
import pandas as pd

# Load saved model
model = mlflow.pyfunc.load_model("model")

# Example input (take first row of dataset schema)
sample = pd.DataFrame([{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984126984,
    "AveBedrms": 1.023809524,
    "Population": 322.0,
    "AveOccup": 2.555555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}])

print("Input:")
print(sample)
print("Prediction:", model.predict(sample))