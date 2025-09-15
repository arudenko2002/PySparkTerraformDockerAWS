#To run Kafka on Docker, first confirm your Docker Desktop is running. Then execute the following command from the kafka-on-docker directory:
docker compose up -d
#The -d flag runs the docker container in detached mode which is similar to running Unix commands in the background by appending &.
#To confirm the container is running, run this command:
docker logs broker


#Now let's produce and consume a message! To produce a message, let's open a command terminal on the Kafka container

#Then create a topic:
./kafka-topics.sh --create --topic my-topic --bootstrap-server broker:29092

# Check topics
docker exec -it two_containers-kafka-1 kafka-topics --list --bootstrap-server kafka:9092

#The result of this command should be:
#Created topic my-topic.
#Important
#Take note of the --bootstrap-server flag.
#Because you're connecting to Kafka inside the container, you use broker:29092 for the host:port.
#If you were to use a client outside the container to connect to Kafka,
#a producer application running on your laptop for example, you'd use localhost:9092 instead.

#Next, start a console producer with this command:
./kafka-console-producer.sh  --topic my-topic --bootstrap-server broker:29092

#At the prompt copy each line one at time and paste into the terminal hitting enter key after each one:
>All streams
>lead to Kafka
#Then enter a CTRL-C to close the producer.

#Now let's consume the messages with this command:
./kafka-console-consumer.sh --topic my-topic --from-beginning --bootstrap-server broker:29092

#And you should see the following:
>All streams
>lead to Kafka
#Enter a CTRL-C to close the consumer and then type exit to close the docker shell.

#To shut down the container, run
docker compose down -v