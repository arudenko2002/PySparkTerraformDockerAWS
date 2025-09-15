import requests
import json
import numpy as np

# Example input (Iris dataset)
data = {
    "inputs": np.array([[5.1, 3.5, 1.4, 0.2],[15.1, 13.5, 11.4, 10.2],[115.1, 113.5, 111.4, 110.2],[5.1, 3.5, 991.4, 990.2]]).tolist()
}

response = requests.post(
    url="http://127.0.0.1:1234/invocations",
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)
)

print("Prediction:", response.json())