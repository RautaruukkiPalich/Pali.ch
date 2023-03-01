from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.urlsDB

series_collection = db.urls
