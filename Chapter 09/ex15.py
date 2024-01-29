import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", "r") as afp:
        print(await afp.read())


if __name__ == "__main__":
    asyncio.run(main())
