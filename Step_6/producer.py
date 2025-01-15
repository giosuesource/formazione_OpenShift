from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1))

for _ in range(100):
    producer.send('foobar', b'Messaggio di prova')
