from django.urls import path
from .consumer import ChatApp, AsyncChatApp

websocket_urlpatterns=[
    path('ws/chat/<str:groupName>/',ChatApp.as_asgi()),
    path('ws/aschat/<str:groupName>/',AsyncChatApp.as_asgi()),
]