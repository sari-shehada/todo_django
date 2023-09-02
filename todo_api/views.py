import uuid
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TODO, AppUser
from .serializer import TODOSerializer, AppUserSerializer
# Create your views here.


@api_view(['GET'])
def getTODOs(request):
    todos = TODO.objects.all()
    serializer = TODOSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postTODO(request):
    serializer = TODOSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    userName = request.data.get('userName')
    password = request.data.get('password')
    try:
        user = AppUser.objects.get(userName=userName, password=password)
    except AppUser.DoesNotExist:
        return Response(False)
    return Response(user.id)


@api_view(['PUT'])
def markTODOAsComplete(request):
    todo_id = request.data.get('id')
    try:
        todo = TODO.objects.get(id=todo_id)
    except TODO.DoesNotExist:
        return Response({'Error': 'Todo not found'}, status=404)
    todo.isFinished = True
    todo.save()
    return Response(True)


@api_view(['GET'])
def getUsers(request):
    users = AppUser.objects.all()
    serializer = AppUserSerializer(users, many=True)
    return Response(serializer.data)
