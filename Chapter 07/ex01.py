from threading import Thread
import logging
from time import sleep


class MyThread(Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
    ):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        sleep(2)
        logging.debug("Wake up!")
        logging.debug(f"args: {self.args}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    for i in range(5):
        thread = MyThread(args=(f"Count thread - {i}",))
        thread.start()
    print("Usefull message")
