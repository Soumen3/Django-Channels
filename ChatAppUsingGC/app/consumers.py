from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Chat,Group
from channels.db import database_sync_to_async

class ChatApp(WebsocketConsumer):
    def connect(self):
        print("Wensocket Connected")
        print('Channel Layer:...',self.channel_layer)
        print('Channel Name:...',self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        # Join room group
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Message receive from client:...",text_data)
        data=json.loads(text_data)
        message=data['msg'] 
        print("The message is: ",message)

        #---Authentication--#
        if self.scope['user'].is_authenticated:

            # saving the message in database
            group=Group.objects.filter(name=self.group_name).first()
            chat=Chat(
                content=message,
                group=group
            )
            chat.save()
            
            # send to all clients connected with this group name 
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,{
                    'type':'chat_message',
                    'message':message
                }
            )
        else:
            self.send(text_data=json.dumps({'msg':"Login Required"}))

    def chat_message(self, event):
        print(event)
        message = event['message']
        print(message)
        print("Sending to Client :..",message)
        self.send(text_data=json.dumps({'msg':message}))



    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)




class AsyncChatApp(AsyncWebsocketConsumer):
    async def connect(self):
        print("Wensocket Connected")
        print('Channel Layer:...',self.channel_layer)
        print('Channel Name:...',self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        # Join room group
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("Message receive from client:...",text_data)
        data=json.loads(text_data)
        message=data['msg'] 
        print("The message is: ",message)

        if self.scope['user'].is_authenticated:
            # saving the message in database
            await database_sync_to_async(self.save_chat_message)(message)
            
            # send to all clients connected with this group name 
            await self.channel_layer.group_send(
                self.group_name,{
                    'type':'chat_message',
                    'message':message
                }
            )
        else:
            await self.send(text_data=json.dumps({'msg':"Login Required"}))
        
    async def chat_message(self, event):
        print(event)
        message = event['message']
        print(message)
        print("Sending to Client :..",message)
        await self.send(text_data=json.dumps({'msg':message}))

    def save_chat_message(self,message):
        print('message: ',message)
        print('typr: ',type(message))
        GroupName= Group.objects.filter(name=self.group_name).first()
        if not GroupName:
            GroupName= Group(name=self.group_name)
            GroupName.save()
            chat=Chat(
                content=message,
                group=GroupName
            )
        else:
            chat=Chat(
                content=message,
                group=GroupName
            )
        chat.save()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
