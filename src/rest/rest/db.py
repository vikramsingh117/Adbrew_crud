import os
from pymongo import MongoClient  # type: ignore

mongo_uri = f"mongodb://{os.environ['MONGO_HOST']}:{os.environ['MONGO_PORT']}"
db = MongoClient(mongo_uri)['test_db']
