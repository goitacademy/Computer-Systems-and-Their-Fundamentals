import asyncio


async def long_running_task():
    try:
        # Припустимо, ця операція триває довго
        await asyncio.sleep(10)
        return "Завдання завершено"
    except asyncio.CancelledError:
        print("Завдання було скасовано")
        raise


async def main():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(1)  # Чекаємо деякий час перед скасуванням
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Головна програма: Завдання скасовано")


if __name__ == "__main__":
    asyncio.run(main())
