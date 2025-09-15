#Create model, train model (fit), predict, verify accuracy.  No logging  and regstration.  Model is about the classification of flowers.
python train.py
#Create, log and register model
python train_register.py
#http://localhost:5000/
# mlflow.sklearn.log_model( does 3 things:
#Saves the model to mlruns/<experiment_id>/<run_id>/artifacts/model/
#Logs the model as an artifact under your MLflow run
#Registers the model as IrisClassifier if the Model Registry is enabled


#list model versions
python list_models.py


# check models and run id
python check_models.py
# ['IrisClassifier']
# Version: 7, Run ID: 5dcf77d2f5e14847af979bbbb04b8bd4, Source: models:/m-768a230f93144916ac3c7927e8da088f

$env:MLFLOW_TRACKING_URI = "sqlite:///C:/Users/AlexR/PycharmProjects/pythonProject/mlflow/mlruns.db"
mlflow models serve -m models:/IrisClassifier/1 -p 1234  # put model into service

# run predictions - it will predict what flower it is - classification [0,1,2,3] - flower ids
python predictions.py
# Prediction: {'predictions': [0, 2, 2, 2]}
# or
curl -X POST http://localhost:1234/invocations `
  -H "Content-Type: application/json" `
  -d '{"inputs": [[5.1, 3.5, 1.4, 0.2]]}'

# Docker
# built in utility to generate DOcker image
# -m: path to the saved model
# -n: name for the Docker image
mlflow models build-docker -m ./iris_model -n iris-classifier
# run the image above
docker run -p 1234:8080 iris-classifier
# http://localhost:1234/invocations
