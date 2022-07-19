from django.urls import path
from .views import UserListAPIView, UserCreateAPIView

urlpatterns = [
    path('list/', UserListAPIView.as_view()),
    path('create/', UserCreateAPIView.as_view()),
]
