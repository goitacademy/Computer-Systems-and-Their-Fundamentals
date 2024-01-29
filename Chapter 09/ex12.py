import requests
from time import time

urls = ["http://www.google.com", "http://www.python.org", "http://duckduckgo.com"]


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


if __name__ == "__main__":
    start = time()
    for url in urls:
        r = preview_fetch(url)
        print(r)
    print(time() - start)
