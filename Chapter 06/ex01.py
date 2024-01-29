from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)

db = client.book

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)
