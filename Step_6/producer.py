from kafka import KafkaProducer

print('above producer')
producer = KafkaProducer(bootstrap_servers=['my_ip:9092'], api_version=(0, 10, 1),
                         compression_type=None
                         )
print('after producer')
for _ in range(100):
    producer.send('test', b'HELLO NITHIN chandran')

print('after sending messages')
