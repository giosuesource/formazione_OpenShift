from kafka import KafkaConsumer

consumer = KafkaConsumer('test', group_id='test-consumer-group', 
bootstrap_servers=['my_ip:9092'], api_version=(0, 10, 1),
                     auto_offset_reset='earliest')
print("Consuming messages")
for msg in consumer:
    print(msg)
