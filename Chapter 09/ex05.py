import asyncio


async def faulty_task():
    raise ValueError("Помилка у завданні")


async def main():
    task = asyncio.create_task(faulty_task())

    try:
        await task
    except ValueError as e:
        print(f"Виняток під час виконання завдання: {e}")
    else:
        print(f"Завдання завершилося успішно: {task.result()}")


if __name__ == "__main__":
    asyncio.run(main())
