from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
              # api_version=(0,11,5),
              # value_serializer=lambda x: dumps(x).encode('utf-8'))

topic = 'test-topic'

# Send some messages
i = 0
while True:
    message = f"Hello Kafka {i}"
    message2 = ('{"value":"'+message+'"}').encode('utf-8')
    producer.send(topic, message2)
    print(f"Sent: {message2}")
    i += 1
    time.sleep(1)

producer.flush()
producer.close()
