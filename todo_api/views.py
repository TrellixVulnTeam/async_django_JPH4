from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ToDo
from .serializers import ToDoSerializer

@api_view(['GET'])
def getRoutes(request):
    
    
    routes = [
        {
            'Endpoint': '/api/todo/list',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/api/todo/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/api/todo/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/api/todo/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/api/todo/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    
    return Response(routes)

@api_view(['GET'])
def getToDoList(request):
    todo_list = ToDo.objects.all().order_by('-updated')
    serializer = ToDoSerializer(todo_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getToDo(request, pk):
    todo = ToDo.objects.get(id=pk)
    serializer = ToDoSerializer(todo, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateToDo(request, pk):
    data = request.data # the json data
    todo = ToDo.objects.get(id=pk)
    serializer = ToDoSerializer(instance=todo, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)