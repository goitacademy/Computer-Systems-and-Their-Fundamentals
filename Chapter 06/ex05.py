from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = client.book

db.cats.delete_one({"name": "barsik"})
result = db.cats.find_one({"name": "barsik"})
print(result)
