from django.urls import path
from .views import ListApiView, CreateApiView

urlpatterns = [
    path('api/list/', ListApiView.as_view()),
    path('api/create/', CreateApiView.as_view())
]