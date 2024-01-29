from multiprocessing import Manager, Process
import time


def modify_first(shared_list):
    shared_list[0]["key1"] = "modified by first process"
    print("First Process: Modified the first dictionary")


def modify_third(shared_list):
    shared_list[2]["key3"] = "modified by third process"
    print("Third Process: Modified the third dictionary")


def read(shared_list):
    # Чекаємо деякий час, щоб зміни були внесені
    time.sleep(2)
    readable_list = [dict(proxy_dict) for proxy_dict in shared_list]
    print(f"Read Process: Read the shared list - {readable_list}")


if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list(
            [
                manager.dict({"key1": "original1"}),
                manager.dict({"key2": "original2"}),
                manager.dict({"key3": "original3"}),
            ]
        )
        p1 = Process(target=modify_first, args=(shared_list,))
        p2 = Process(target=modify_third, args=(shared_list,))
        p3 = Process(target=read, args=(shared_list,))

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()
