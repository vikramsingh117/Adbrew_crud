from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient
from .repositories.todo_repo import TodoRepository

class TodoListView(APIView):
    def get(self, request):
        try:
            todos = TodoRepository.get_all()
            return Response(todos, status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception("Failed to fetch todos")
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            payload = request.data
            if not payload.get("title"):
                return Response({"detail": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
            todo = TodoRepository.create(payload)
            return Response(todo, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception("Failed to create todo")
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)