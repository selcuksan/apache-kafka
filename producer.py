from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8"))

for num in range(500):
    data = {"num": num}
    producer.send(topic="testnum", value=data)
    sleep(5)
