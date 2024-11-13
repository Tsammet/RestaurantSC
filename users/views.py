from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


# Create your views here.

@api_view(['POST'])
def registerUser(request):

    # SE RECIBEN LOS DATOS DEL REQUEST CON EL RQUEST.DATA Y LUEGO SE PASAN AL REGISTERSERIALIZER PARA QUE COMIENCE LA VALIDACIÓN
    serializer = RegisterSerializer(data = request.data)

    if serializer.is_valid():
        #GUARDA EL USUARIO
        user = serializer.save()

        token = Token.objects.create(user = user)
        
        return Response({'token': token.key, "user": serializer.data}, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def loginUser(request):

    serializer = LoginSerializer(data = request.data)

    if serializer.is_valid():

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user = user)

        return Response({'token':token.key, 'username': user.username, }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
