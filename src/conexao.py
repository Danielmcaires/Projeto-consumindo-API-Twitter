from pymongo import MongoClient

client = MongoClient('mongodb://daniel:daniel@mongo:27017/')
db = client.projeto_twitter
trends_collection = db.trends