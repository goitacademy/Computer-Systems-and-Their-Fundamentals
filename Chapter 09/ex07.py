import asyncio


async def my_task():
    return "Результат завдання my_task"


def my_callback(task):
    print("Завдання завершено з результатом:", task.result())


async def main():
    task = asyncio.create_task(my_task())
    task.add_done_callback(my_callback)
    r = await task
    print(r)


if __name__ == "__main__":
    asyncio.run(main())
