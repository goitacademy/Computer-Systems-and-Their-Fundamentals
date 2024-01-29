import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile


async def main():
    apath = AsyncPath("hello.txt")
    if await apath.exists():
        new_path = AsyncPath("logs")
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(apath, new_path / apath)


if __name__ == "__main__":
    asyncio.run(main())
