from kafka import KafkaConsumer

consumer = KafkaConsumer('foobar', group_id='gruppo-consumer', 
bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', api_version=(0, 10, 1)) 

for msg in consumer:
    print(msg)
