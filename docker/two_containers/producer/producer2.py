from kafka import KafkaProducer
import time

server = "localhost:9094"
producer = KafkaProducer(bootstrap_servers=server)

for i in range(1000):
    message = f"Message {i} {server}".encode('utf-8')
    producer.send('test-topic', message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()