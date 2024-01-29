import asyncio


async def long_running_task():
    await asyncio.sleep(5)  # Припустимо, що ця операція триває 5 секунд
    return "Завдання завершено"


async def main():
    try:
        # Чекаємо завершення завдання протягом максимум 3 секунд
        result = await asyncio.wait_for(long_running_task(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("Завдання не було завершено вчасно")


if __name__ == "__main__":
    asyncio.run(main())
