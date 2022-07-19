from django.db import models


class User(models.Model):
    tele_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
