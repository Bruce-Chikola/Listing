from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Friends(models.Model):
    user_id = models.IntegerField(default=0)
    # user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    friend_id = models.IntegerField(default=0)
