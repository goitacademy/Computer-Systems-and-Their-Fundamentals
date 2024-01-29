import asyncio


async def baz() -> str:
    print("Before Sleep")
    await asyncio.sleep(1)
    print("After Sleep")
    return "Hello world"


async def main():
    r = baz()
    print(r)
    result = await r
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
