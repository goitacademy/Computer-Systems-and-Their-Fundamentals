import asyncio


async def task_one():
    await asyncio.sleep(1)
    return "результат task_one"


async def task_two():
    await asyncio.sleep(2)
    return "результат task_two"


async def main():
    tasks = [asyncio.create_task(task) for task in [task_one(), task_two()]]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print("Завершено:", task.result())


if __name__ == "__main__":
    asyncio.run(main())
