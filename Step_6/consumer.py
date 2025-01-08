from kafka import KafkaConsumer

consumer = KafkaConsumer('foobar', group_id='gruppo-consumer', 
bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest') 

for msg in consumer:
    print(msg)
