from rest.db import db


class TodoReader:
    @staticmethod
    def get_all():
        todos = []
        for doc in db.todos.find():
            item = dict(doc)
            if '_id' in item:
                item['_id'] = str(item['_id'])
            todos.append(item)
        return todos
    
