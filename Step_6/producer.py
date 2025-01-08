from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['my_ip:9092'])

for _ in range(100):
    producer.flush('foobar', b'Messaggio di prova')
