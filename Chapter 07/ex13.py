from random import randint
from threading import Thread, Barrier
import logging
from time import sleep, ctime


def worker(barrier: Barrier):
    logging.debug(f"Start thread: {ctime()}")
    sleep(randint(1, 3))  # Simulate some work
    r = barrier.wait()
    logging.debug(f"count: {r}")
    logging.debug(f"Barrier overcome: {ctime()}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    barrier = Barrier(5)

    for num in range(10):
        thread = Thread(name=f"Th-{num}", target=worker, args=(barrier,))
        thread.start()
