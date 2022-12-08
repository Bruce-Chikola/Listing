from django.db import models


class Friends(models.Model):
    user_id = models.IntegerField(default=0)
    friend_id = models.IntegerField(default=0)
