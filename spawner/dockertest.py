import docker
import pika
from sys import argv,exit

if len(argv) < 2:
    print("specify queue")
    exit()

queue = argv[1]
envs = ["DOCKER=True", f"QUEUE={queue}"]

credentials = pika.PlainCredentials('admin', 'mypass')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=queue,durable=True)
connection.close()

client = docker.from_env()
client.containers.run(
    "dyn_worker",
    volumes={"/home/shane/playground/docker/dyn_workers/logs":
        {
            'bind':'/logs/','mode':'rw'}
        },
    network='dyn_workers_default',
    environment=envs,
    detach=True
)
