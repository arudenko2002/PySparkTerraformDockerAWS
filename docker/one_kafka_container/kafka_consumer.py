from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='my-group'
)

print("Listening for messages...")
for num,message in enumerate(consumer):
    print(f"Received: {num} {message.value}")
    print(message.value["value"])