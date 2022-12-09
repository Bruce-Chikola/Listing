import graphene
from graphene_django import DjangoObjectType
from .models import Friends
# am usign the default django user Model as friends and everything else
from django.contrib.auth import get_user_model

User = get_user_model()

# OPERATIONS ON THE USER MODELS


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", 'first_name', 'last_name', 'username', 'email')


# OPERATIONS ON THE FRIENDS MODEL
class FriendsType(DjangoObjectType):
    class Meta:
        model = Friends
        fields = ("id", 'user_id', 'friend_id')


class FriendsMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        friend_id = graphene.Int(required=True)
    friend = graphene.Field(FriendsType)

    @classmethod
    def mutate(cls, root, info, user_id, friend_id):
        print(user_id)
        friend = Friends(userId=user_id, friendId=friend_id)
        friend.save()
        return FriendsMutation(friend)


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_friends = graphene.List(FriendsType)
    user_by_email = graphene.Field(UserType, param=graphene.String())

    def resolve_all_users(root, info):
        return User.objects.all()

# to search for a user buy email or username
    def resolve_user_by_email(root, info, param):
        if '@' in param:
            return User.objects.get(email=param)
        else:
            return User.objects.get(username=param)


# to fetch friends


    def resolve_all_friends(root, info):
        return Friends.objects.all()


# to add new content to the models
class Mutation(graphene.ObjectType):
    add_new_friend = FriendsMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
