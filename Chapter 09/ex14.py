import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", "w+") as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - async world!")


if __name__ == "__main__":
    asyncio.run(main())
