from threading import Timer
import logging
from time import sleep


def example_work():
    logging.debug("Start!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

    first = Timer(0.5, example_work)
    first.name = "First thread"
    second = Timer(0.7, example_work)
    second.name = "Second thread"
    logging.debug("Start timers")
    first.start()
    second.start()
    sleep(0.6)
    second.cancel()

    logging.debug("End program")
