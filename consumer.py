import pika
import json
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('34.88.223.172'))
channel = connection.channel()
channel.queue_declare(queue='eco_delivery')

def callback(ch, method, properties, body):
    task = json.loads(body)
    print(f" [x] Picked up task {task['task_id']} — Delivering from {task['pickup']} to {task['dropoff']}")
    time.sleep(2)  # simulate delivery time
    print(f" [✓] Delivered {task['task_id']}")

channel.basic_consume(queue='eco_delivery', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for eco-delivery tasks. Press CTRL+C to exit.')
channel.start_consuming()

