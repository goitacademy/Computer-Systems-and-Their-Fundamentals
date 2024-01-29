from multiprocessing import Process
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class MyProcess(Process):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
    ):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self) -> None:
        logger.debug(self.args)


def example_work(params):
    sleep(0.5)
    logger.debug(params)


if __name__ == "__main__":
    processes = []
    for i in range(3):
        pr = Process(target=example_work, args=(f"Count process function - {i}",))
        pr.start()
        processes.append(pr)

    for i in range(2):
        pr = MyProcess(args=(f"Count process class - {i}",))
        pr.start()
        processes.append(pr)

    [el.join() for el in processes]
    [print(el.exitcode, end=" ") for el in processes]
    logger.debug("End program")
