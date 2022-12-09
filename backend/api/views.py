from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
User = get_user_model()


# to login
@api_view(['POST'])
@permission_classes([AllowAny])
def API_Login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response(data="success", status=status.HTTP_200_OK)
    return Response(data="faild", status=status.HTTP_502_BAD_GATEWAY)


class LoggedInUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        data = serializer.data
        return Response(data)


# # to add a new friend to the friends list
# @api_view(['POST'])
# def AddNewFriend(request):
#     serializer = FriendsSerializer(data=request.data)
#     if serializer.is_valid():
#         save = serializer.save()
#         return Response(data={'status': 200}, status=status.HTTP_200_OK)
#     else:
#         return Response(data={'status': 500}, status=status.HTTP_502_BAD_GATEWAY)


# # unfriend/delete the friend record
# @api_view(['POST'])
# def Unfriend(request):
#     relation = Friends.objects.get(id=request.data['id'])
#     relation.delete()
#     return Response(data={'status': 200}, status=status.HTTP_200_OK)
