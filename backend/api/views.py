from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializer import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
User = get_user_model()


# class FriendsView(generics.ListAPIView):
#     queryset = Friends.objects.all()
#     serializer_class = FriendsSerializer


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


# @permission_classes((IsAuthenticated,))
# class UserList(APIView):
#     def get(self, request):
#         userList = User.objects.all()
#         serializer = UserSerializer(userList, many=True)
#         data = serializer.data
#         userInfo = []
#         if len(data) > 0:
#             for user in data:
#                 friends = UserFriendsView(request, user['id'])
#                 userInfo.append({'user': user, 'friends': friends.data})
#         return Response(data=userInfo, status=status.HTTP_200_OK)


# def UserFriendsView(request, pk):
#     userList = Friends.objects.filter(user_id=pk)
#     serializer = FriendsSerializer(userList, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


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


# # unfriend/delete the friend record
# # to manually delete a record from friends relation, navigate to http://127.0.0.1:8000/api/delete/{pass in the ID Here}
# @api_view(['DELETE'])
# def Delete(request, pk):
#     relation = Friends.objects.get(id=pk)
#     relation.delete()
#     return Response(data={'status': 200}, status=status.HTTP_200_OK)
