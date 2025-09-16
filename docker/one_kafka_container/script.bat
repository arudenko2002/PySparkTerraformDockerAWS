#load the image from Docker Hub
REM Get the Docker image:
$ docker pull apache/kafka:4.0.0

REM Start the Kafka Docker container:
$ docker run -p 9092:9092 apache/kafka:4.0.0