from custom_module import logger
from custom_module.celery import app
from time import sleep


@app.task()
def dummy():
    logger.info('log from custom modules')
    sleep(30)