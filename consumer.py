import pika
import json
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('34.88.223.172'))
channel = connection.channel()

# Declare durable queue (must match producer)
channel.queue_declare(queue='eco_delivery', durable=True)

def callback(ch, method, properties, body):
    task = json.loads(body)
    print(f"[🚴] {task['task_id']} — From {task['pickup']} to {task['dropoff']}")

    # Simulate variable delivery time
    time.sleep(random.uniform(0.5, 2.0))

    print(f"[✓] Delivered {task['task_id']}\n")

    # Acknowledge the message was processed
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Fair dispatch: don't send more than one message to a worker until it finishes the previous one
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='eco_delivery', on_message_callback=callback)

print('[*] Waiting for delivery tasks. To exit press CTRL+C')
channel.start_consuming()

