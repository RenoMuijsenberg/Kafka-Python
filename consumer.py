from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': "host.docker.internal:9092",
    'group.id': 'test',
    'auto.offset.reset': 'earliest',
})

# Subscribe to the topic
consumer.subscribe(["Brett"])

try:
    # Start consuming messages
    while True:
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition, consumer reached end of topic
                continue
            else:
                # Some other error
                print(msg.error())
                break

        # Process the received message
        print('Received message: {}'.format(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    print(f"Interrupted by user")
    consumer.close()
except Exception as e:
    print(f"An error occurred: {e}")
    consumer.close()
