from pymongo import MongoClient
from pydantic import BaseModel

MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
database = client.log_collector
print("connected successfully")