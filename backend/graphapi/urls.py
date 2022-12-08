from django.urls import path, include
from graphene_django.views import GraphQLView
# from graphapi.schema import schema
urlpatterns = [
    path('/', GraphQLView.as_view(graphiql=True))
]
