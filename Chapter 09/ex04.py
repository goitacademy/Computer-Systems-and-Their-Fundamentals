import asyncio
import random


async def random_value():
    print("start task")
    await asyncio.sleep(1)
    print("task finished")
    return random.random()


async def main():
    task = asyncio.create_task(random_value())
    print("task scheduled")
    await task
    print(f"result: {task.result()}")


if __name__ == "__main__":
    asyncio.run(main())
