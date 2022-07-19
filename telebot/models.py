from django.db import models


class Telebot(models.Model):
    tele_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=221)
    user_name = models.CharField(max_length=221)
    created_at = models.DateTimeField(auto_now_add=True)

