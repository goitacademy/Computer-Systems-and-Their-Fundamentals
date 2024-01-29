import requests


r = requests.get("https://api.github.com/events")
print(r.text[:300])
