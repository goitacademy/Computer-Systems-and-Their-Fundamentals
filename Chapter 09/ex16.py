import asyncio
from aiofile import AIOFile, LineReader


async def main():
    async with AIOFile("hello.txt", "r") as afp:
        async for line in LineReader(afp):
            print(line)


if __name__ == "__main__":
    asyncio.run(main())
