FROM python:3
COPY ./requirements.txt /custom_module/requirements.txt
RUN pip3 install -r ./custom_module/requirements.txt
COPY ./* /custom_module
ENTRYPOINT celery -A custom_module worker --concurrency=1 --loglevel=info --pool=gevent -Q $QUEUE
