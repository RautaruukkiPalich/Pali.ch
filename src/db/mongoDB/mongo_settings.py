import os

from pymongo import MongoClient

uri = os.environ.get("DB_URI", "mongodb://localhost:27017")
client = MongoClient(uri)

db = client.urlsDB

series_collection = db.urls
