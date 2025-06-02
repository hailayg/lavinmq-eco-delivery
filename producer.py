import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('34.88.223.172'))
channel = connection.channel()
channel.queue_declare(queue='eco_delivery')

task = {
    'task_id': str(uuid.uuid4()),
    'pickup': 'Central Station',
    'dropoff': 'Museum of Technology',
    'package_weight': '2.1kg',
    'eco_mode': 'bike'
}

channel.basic_publish(
    exchange='',
    routing_key='eco_delivery',
    body=json.dumps(task)
)

print(f" [x] Sent delivery task {task['task_id']}")
connection.close()

