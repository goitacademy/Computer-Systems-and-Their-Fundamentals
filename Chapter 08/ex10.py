from multiprocessing import Pool, current_process
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(x):
    logger.debug(f"pid={current_process().pid}, x={x}")
    return x * x


if __name__ == "__main__":
    with Pool(processes=2) as pool:
        logger.debug(pool.map(worker, range(10)))
