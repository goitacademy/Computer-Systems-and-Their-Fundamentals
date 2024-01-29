from threading import Thread
from time import sleep
import logging


def example_work(delay):
    sleep(delay)
    logging.debug("Wake up!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    for i in range(5):
        thread = Thread(target=example_work, args=(i,))
        thread.start()
