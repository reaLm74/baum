from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:9092')


# Отправка сообщения в kafka
async def send_data(topic, key, value) -> None:
    producer.send(topic, key=key, value=value)
