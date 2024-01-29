import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from time import time

urls = ["http://www.google.com", "http://www.python.org", "http://duckduckgo.com"]


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(3) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result


if __name__ == "__main__":
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(time() - start)
