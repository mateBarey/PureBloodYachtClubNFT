from pymongo import MongoClient
from config import Config 

client = MongoClient(Config.MONGO_DATABASE_URI)
db = client.SimlarityDB

users = db["Users"]