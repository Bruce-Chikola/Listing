import graphene
from graphene_django import DjangoObjectType
from .models import Friends
# am usign the actual user Model as friends and everything else
from django.contrib.auth import get_user_model

User = get_user_model()

# OPERATIONS ON THE USER MODEL


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
    friendData = graphene.Field(FriendsType)

    @classmethod
    def mutate(cls, root, info):
        f = Friends()
        f.save()
        return FriendsMutation(f)


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_friends = graphene.List(FriendsType)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_friends(root, info):
        return Friends.objects.all()


# to add new content to the models
class Mutation(graphene.ObjectType):
    add_new_friend = FriendsMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
