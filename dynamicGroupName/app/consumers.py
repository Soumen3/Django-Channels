
# Topic Chat app

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
import json
import time
import asyncio
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connected...")
        # get default channel layer from a project
        print("Channel Layer: ", self.channel_layer)
        # get default channel name from a project
        print("Channel name: ", self.channel_name)

        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name.... ", self.group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name)
        self.send({
            'type': "websocket.accept"
        })

    def websocket_receive(self, event):
        print("Message recieve from client: ", event['text'])

        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            "type": "chat.message",
            'message': event['text']
        })

    def chat_message(self, event):
        print('Event...', event)
        print('Actual data...', event['message'])
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        # get default channel layer from a project
        print("Channel Layer: ", self.channel_layer)
        # get default channel name from a project
        print("Channel name: ", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name)
        print("Websocket disonnected...")

        raise StopConsumer


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected...")
        # get default channel layer from a project
        print("Channel Layer: ", self.channel_layer)
        # get default channel name from a project
        print("Channel name: ", self.channel_name)

        await self.channel_layer.group_add('programmers', self.channel_name)
        await self.send({
            'type': "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("Message recieve from client: ", event['text'])

        await self.channel_layer.group_send('programmers', {
            "type": "chat.message",
            'message': event['text']
        })

    async def chat_message(self, event):
        print('Event...', event)
        print('Actual data...', event['message'])
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        # get default channel layer from a project
        print("Channel Layer: ", self.channel_layer)
        # get default channel name from a project
        print("Channel name: ", self.channel_name)
        await self.channel_layer.group_discard('programmers', self.channel_name)
        print("Websocket disonnected...")

        raise StopConsumer
