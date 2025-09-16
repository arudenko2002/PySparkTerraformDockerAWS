@REM Create model, train model (fit), predict, verify accuracy.  No logging  and regstration.  Model is about the classification of flowers.
python train.py
@REM Create, log and register model
python train_register.py
@REM http://localhost:5000/
@REM  mlflow.sklearn.log_model( does 3 things:
@REM Saves the model to mlruns/<experiment_id>/<run_id>/artifacts/model/
@REM Logs the model as an artifact under your MLflow run
@REM Registers the model as IrisClassifier if the Model Registry is enabled


@REM list model versions
python list_models.py


@REM check models and run id
python check_models.py
@REM ['IrisClassifier']
@REM Version: 7, Run ID: 5dcf77d2f5e14847af979bbbb04b8bd4, Source: models:/m-768a230f93144916ac3c7927e8da088f

$env:MLFLOW_TRACKING_URI = "sqlite:///C:/Users/AlexR/PycharmProjects/pythonProject/mlflow/mlruns.db"
mlflow models serve -m models:/IrisClassifier/1 -p 1234  # put model into service

@REM run predictions - it will predict what flower it is - classification [0,1,2,3] - flower ids
python predictions.py
@REM Prediction: {'predictions': [0, 2, 2, 2]}
@REM or
curl -X POST http://localhost:1234/invocations \
  -H "Content-Type: application/json" \
  -d '{"inputs": [[5.1, 3.5, 1.4, 0.2]]}'

@REM Docker
@REM built in utility to generate DOcker image
@REM -m: path to the saved model
@REM -n: name for the Docker image
mlflow models build-docker -m ./iris_model -n iris-classifier
@REM # run the image above
docker run -p 1234:8080 iris-classifier
@REM # http://localhost:1234/invocations

docker build -t arudenko2002/iris-classifier:latest .
docker push arudenko2002/iris-classifier:latest
kubectl delete pod iris-classifier
kubectl apply -f .\iris-classifier.yaml
kubectl get pods
@REM NAME                                READY   STATUS             RESTARTS        AGE
@REM flask-deployment-7f78dd679b-p765x   1/1     Running            0               24h
@REM iris-classifier-d9d7cc59d-qvjdz     0/1     CrashLoopBackOff   7 (4m46s ago)   16m
@REM nginx-5869d7778c-858t2              1/1     Running            0               22h
@REM nginx-deployment-84444954cd-5fnbf   1/1     Running            0               22h

kubectl logs deployment/iris-classifier
kubectl get svc iris-service
@REM NAME           TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
@REM iris-service   NodePort   10.102.112.198   <none>        1234:30815/TCP   9h
kubectl port-forward service/iris-service 1234:1234
python predictions.py


mlflow models serve -m models:/IrisClassifier/7 -p 1234


@REM SSH to pod and execute netstat -tuln
kubectl get pods
@REM NAME                                READY   STATUS    RESTARTS      AGE
@REM flask-deployment-7f78dd679b-p765x   1/1     Running   0             39h
@REM iris-classifier-d9d7cc59d-qvjdz     1/1     Running   8 (14h ago)   15h
@REM nginx-5869d7778c-858t2              1/1     Running   0             36h
@REM nginx-deployment-84444954cd-5fnbf   1/1     Running   0             37h
(.venv) PS C:\Users\AlexR\PycharmProjects\pythonProject\kubernetes\mlflow-app> kubectl exec -it iris-classifier-d9d7cc59d-qvjdz -- /bin/bash
root@iris-classifier-d9d7cc59d-qvjdz:/# netstat -tuln
@REM Active Internet connections (only servers)
@REM Proto Recv-Q Send-Q Local Address           Foreign Address         State
@REM tcp        0      0 0.0.0.0:1234            0.0.0.0:*               LISTEN
root@iris-classifier-d9d7cc59d-qvjdz:/#


My project:
@REM Create, log and register model
python train_register.py
docker build -t arudenko2002/iris-classifier:latest .
docker tag iris-classifier arudenko2002/iris-classifier:latest
docker push arudenko2002/iris-classifier:latest
kubectl delete pod iris-classifier
kubectl apply -f .\iris-classifier.yaml
kubectl port-forward service/iris-service 1234:1234
python predictions.py


