from confluent_kafka import Consumer

server = 'localhost:9094'
conf = {
    'bootstrap.servers': server,
    'group.id': 'external-group',
    'auto.offset.reset': 'earliest',
}
consumer = Consumer(conf)
consumer.subscribe(['test-topic'])

while True:
    msg = consumer.poll(1.0)
    if msg:
        print("received", msg.value().decode('utf-8'))