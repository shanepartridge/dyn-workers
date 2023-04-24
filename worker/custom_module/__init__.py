from socket import gethostname
from pathlib import Path

import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    f'[{gethostname()}]- %(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
)

logpath = Path('./logs')
if not logpath.exists() or logpath.exists() and logpath.is_dir() is False:
    logpath.mkdir()

filepath = logpath / f'{gethostname()}_worker_log.txt'
fh = logging.FileHandler(filepath)
fh.setFormatter(formatter)
logger.addHandler(fh)


in_docker = os.getenv("DOCKER", False)
