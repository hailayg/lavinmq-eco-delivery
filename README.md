# LavinMQ Eco-Delivery Queue 🚴‍♂️

A real-time task queuing demo built for the LavinMQ Green Slope 1-Day Hackathon Challenge.

## What it Does

Simulates a dispatcher assigning eco-friendly delivery tasks (e.g. bike courier jobs) using LavinMQ.

- `producer.py`: Dispatches a new delivery job.
- `consumer.py`: Picks up and "delivers" the job.

## Tech Stack

- LavinMQ (via Docker)
- Python
- Pika (AMQP client)
- GCP VM with Docker

## How to Run

1. Run LavinMQ using Docker:

```bash
docker run -d --name lavinmq -p 5672:5672 -p 15672:15672 cloudamqp/lavinmq
Concept:
Build a lightweight task queue system that simulates eco-deliveries (e.g., bike couriers delivering packages in a green city). Use LavinMQ to queue tasks like “deliver package from A to B” and simulate workers consuming those tasks.

This aligns with sustainability, mobility, and messaging systems – all good hackathon themes.
