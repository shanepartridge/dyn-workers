Example of adding new containers to an existing network from within a docker container

## Set up

RabbitMQ and Flower server in docker-compose.yml

Build the worker and spawner services from within the respective directories.

### worker image

Celery worker using a dummy module that writes a log entry and waits for a time.

```
docker build . -t dyn_worker
```

### Spawner image

Service will be used to add new containers, will contain/run a script using `pika` and `docker` python module.

```
docker build . -t spawner
```

```
docker run --rm -it --network dyn_workers_default -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker spawner bash
```

- Mounts docker socket and docker binary
  - Will require docker to be installed on host system

This will drop you into a bash shell in the spawner container, `/dockertest.py` can be used as `python3 dockertest.py {queue}` to create a new queue and point a new worker at that queue.

- Obviously make sure that the compose services are running
