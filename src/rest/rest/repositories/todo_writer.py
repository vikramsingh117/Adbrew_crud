from rest.db import db


class TodoWriter:
    @staticmethod
    def create(todo_data: dict):
        result = db.todos.insert_one(todo_data)
        todo_data['_id'] = str(result.inserted_id)
        return todo_data
