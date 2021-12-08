from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .models import ToDolist
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/todolist/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of todo'
        },
        {
            'Endpoint': '/todolist/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/todolist/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/todolist/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/todolist/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getToDoList(request):
    todo = ToDolist.objects.all()

    return Response('todo')