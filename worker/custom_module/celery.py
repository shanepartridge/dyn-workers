from custom_module import in_docker
from celery import Celery

hostname = 'localhost' if in_docker is False else 'rabbit'
app = Celery(
        'custom_module',
        broker=f'amqp://admin:mypass@{hostname}:5672',
        include=['custom_module.tasks']
    )
