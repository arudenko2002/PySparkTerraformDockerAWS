#put model into docker image
mlflow models build-docker -m "models:/IrisClassifier/9" -n iris-classifier
# tag and register the image to DockerHub
docker tag iris-classifier arudenko2002/iris-classifier:latest
docker push arudenko2002/iris-classifier:latest
