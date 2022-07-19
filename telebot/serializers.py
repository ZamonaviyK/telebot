from rest_framework import serializers
from .models import Telebot


class TeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telebot
        fields = ('id', 'tele_id', 'name', 'user_name', 'created_at')