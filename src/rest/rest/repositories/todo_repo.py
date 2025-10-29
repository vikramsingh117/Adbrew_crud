from pymongo import MongoClient
import os

mongo_uri = f"mongodb://{os.environ['MONGO_HOST']}:{os.environ['MONGO_PORT']}"
db = MongoClient(mongo_uri)['test_db']

class TodoRepository:
    @staticmethod
    def get_all():
        todos = []
        for doc in db.todos.find():
            doc['_id'] = str(doc['_id'])
            todos.append(doc)
        return todos

    @staticmethod
    def create(todo_data):
        result = db.todos.insert_one(todo_data)
        todo_data['_id'] = str(result.inserted_id)
        return todo_data
