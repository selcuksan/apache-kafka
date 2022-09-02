from json import loads
from kafka import KafkaConsumer

from database import collection

consumer = KafkaConsumer(
    'testnum',
    bootstrap_servers=['localhost : 9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for msg in consumer:
    message = msg.value
    print(msg, message)
    collection.insert_one(message)
    print(message, "added to", collection, sep=" ")
