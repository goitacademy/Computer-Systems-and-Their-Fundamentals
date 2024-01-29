import asyncio
from aiopath import AsyncPath


async def main():
    apath = AsyncPath("hello.txt")
    print(await apath.exists())
    print(await apath.is_file())
    print(await apath.is_dir())


if __name__ == "__main__":
    asyncio.run(main())
