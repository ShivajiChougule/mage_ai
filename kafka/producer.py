from kafka import KafkaProducer
import json
from data import get_registered_user
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

topic = 'test'
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send(topic, value=registered_user)
        time.sleep(4)