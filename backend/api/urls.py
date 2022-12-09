from django.urls import path
from .views import API_Login, LoggedInUserView
urlpatterns = [
    path('', API_Login),
    path(r'/login', API_Login),
    path(r'/user', LoggedInUserView.as_view()),
]
