import concurrent.futures
import logging
from random import randint
from time import sleep


def greeting(name):
    logging.debug(f"greeting for: {name}")
    sleep(randint(0, 3))
    return f"Hello {name}"


arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(greeting, arguments))

    logging.debug(results)
