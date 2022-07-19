from django.shortcuts import render
from rest_framework import generics

from .models import Telebot
from .serializers import TeleSerializer


class ListApiView(generics.ListAPIView):
    queryset = Telebot.objects.all()
    serializer_class = TeleSerializer


class CreateApiView(generics.CreateAPIView):
    queryset = Telebot.objects.all()
    serializer_class = TeleSerializer
