from custom_module.tasks import dummy
from sys import argv, exit

if len(argv) != 2:
    print("submit a queue to send to")
    exit()

queue = argv[1]
print(f"sending to: {queue}")
dummy.apply_async(queue=queue)