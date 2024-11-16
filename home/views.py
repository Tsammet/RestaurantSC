from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def home(request):

    data = {
        'message': f"Welcome to the application, {request.user.username}!" if request.user.is_authenticated else "Welcome to the application!",
    }
    return Response(data)