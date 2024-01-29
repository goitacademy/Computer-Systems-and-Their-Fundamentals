from multiprocessing import Pipe, Process, current_process
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

recipient1, sender1 = Pipe()
recipient2, sender2 = Pipe()


def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f"{name} started...")
    val = pipe.recv()
    logger.debug(val**2)
    sys.exit(0)


if __name__ == "__main__":
    w1 = Process(target=worker, args=(recipient1,))
    w2 = Process(target=worker, args=(recipient2,))

    w1.start()
    w2.start()

    sender1.send(8)
    sleep(1)
    sender2.send(16)
