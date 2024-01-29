import requests

response = requests.get(
    "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
)
exchange_rate = response.json()
print(exchange_rate)
