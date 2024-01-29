import urllib.request


with urllib.request.urlopen("https://www.python.org/") as f:
    print(f.read(300))
