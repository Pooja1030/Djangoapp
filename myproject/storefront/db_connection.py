# import pymongo

# url = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(url)

# db = client['test_mongo']

from pymongo import MongoClient
import os

mongo_client = MongoClient(
    host=os.getenv('MONGO_DB_HOST', 'mongo'),
    port=int(os.getenv('MONGO_DB_PORT', 27017)),
)

db = mongo_client[os.getenv('MONGO_DB_NAME')]
