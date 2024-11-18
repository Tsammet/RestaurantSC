from django.shortcuts import render
from rest_framework.response import Response
from .models import Reviews
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User


# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def review(request):

    if request.method == "POST":

        data = request.data
        user = request.user

        try:
            review = Reviews.objects.create(
                title = data['title'],
                review = data['review'],
                user = user
            )
            
            return Response({ 'username': review.user.username, "title": review.title, "review" : review.review}, status=status.HTTP_201_CREATED)
        
        except (ValueError, KeyError):
            return Response({"error" :"Error"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":

        reviews = Reviews.objects.all()
        review_data = []
        
        for review in reviews:
            user = User.objects.get(id= review.user_id)
            review_data.append({
                'id' : review.id,
                'title' : review.title,
                'review' : review.review,
                'user' : user.username
            })
        return Response(review_data)