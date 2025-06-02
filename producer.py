import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('34.88.223.172'))
channel = connection.channel()

# Declare a durable queue
channel.queue_declare(queue='eco_delivery', durable=True)

# Send 100 tasks
for i in range(100):
    task = {
        'task_id': str(uuid.uuid4()),
        'pickup': 'Warehouse A',
        'dropoff': f'Destination {i}',
        'package_weight': f'{1 + i % 5}kg',
        'eco_mode': 'bike'
    }

    channel.basic_publish(
        exchange='',
        routing_key='eco_delivery',
        body=json.dumps(task),
        properties=pika.BasicProperties(
            delivery_mode=2  # make message persistent
        )
    )

    print(f" [x] Sent task {task['task_id']}")

connection.close()

