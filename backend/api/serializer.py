from rest_framework import serializers
from .models import Friends
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('__all__')
