from threading import Thread, Event
import logging
from time import sleep


def worker(event: Event):
    logging.debug("Worker ready to work")
    event.wait()
    logging.debug("The worker can do the work")


def master(event: Event):
    logging.debug("Master doing some work")
    sleep(2)
    logging.debug("Informing that workers can do the work")
    event.set()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()
    master = Thread(name="master", target=master, args=(event,))

    worker_one = Thread(name="worker_one", target=worker, args=(event,))
    worker_two = Thread(name="worker_two", target=worker, args=(event,))
    worker_one.start()
    worker_two.start()
    master.start()

    logging.debug("End program")
