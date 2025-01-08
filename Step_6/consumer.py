from kafka import KafkaConsumer

consumer = KafkaConsumer('foobar', group_id='gruppo-consumer', #nome topic e group id
bootstrap_servers=['my_ip:9092'], #ip e porta di Kafka, versione Api
                     auto_offset_reset='earliest') 
print("Consuming messages")
for msg in consumer:
    print(msg)
