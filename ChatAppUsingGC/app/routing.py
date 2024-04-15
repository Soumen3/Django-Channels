from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/chat/<str:groupkaname>/',consumers.ChatApp.as_asgi()),
    path('ws/aschat/<str:groupkaname>/',consumers.AsyncChatApp.as_asgi()),
]