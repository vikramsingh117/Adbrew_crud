from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

class TodoListView(APIView):

    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        # Return all todo items from the `todos` collection.
        # MongoDB ObjectId is not JSON serializable, so convert to string.
        try:
            todos = []
            for doc in db.todos.find():
                if '_id' in doc:
                    doc['_id'] = str(doc['_id'])
                todos.append(doc)
            return Response(todos, status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception("Failed to fetch todos")
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        # Accept a todo item and persist it into the `todos` collection.
        try:
            # request.data can be a QueryDict or dict-like; make a plain dict copy
            payload = request.data.copy() if hasattr(request.data, 'copy') else dict(request.data)

            # Insert into MongoDB
            result = db.todos.insert_one(payload)

            # Return the created document (with _id as string)
            payload['_id'] = str(result.inserted_id)
            return Response(payload, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception("Failed to create todo")
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

