from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.consumer import async_to_sync
from .models import Chat, Group
from channels.db import database_sync_to_async

class ChatApp(JsonWebsocketConsumer):
    def connect(self):
        print("Websocket Connected....")
        self.groupName=self.scope['url_route']['kwargs']['groupName']
        # print("Group name is: ",self.groupName)

        async_to_sync(self.channel_layer.group_add)(self.groupName, self.channel_name)
        self.accept()
        
    
    def receive_json(self, content, **kwargs):
        print('Message Receive from client...',content)
        print("type of the message is: ",type(content))

        message=content['msg']

        if self.scope['user'].is_authenticated:
            # Saving the message in database
            self.save_chat_message(message)

            async_to_sync(self.channel_layer.group_send)(
                self.groupName, 
                {
                    'type': 'chat_message',
                    'text': message
                }
            )
        else:
            self.send_json({"msg":"Login Required"})
        # self.send_json({"msg":"message from server"})
        # self.close(code=4321)       # Froce to close
        
    def chat_message(self, event):
        message=event['text']
        self.send_json({'msg':message})

    def save_chat_message(self, message):
        print("saving message.....")
        group=Group.objects.filter(name=self.groupName).first()
        if group:
            chat = Chat(content=message, group=group)
        else:
            group=Group(name=self.groupName)
            group.save()
            chat = Chat(content=message, group=self.groupName)
        chat.save()

    def disconnect(self, close_code):
        print("Websocket Disconnect....",close_code)
        async_to_sync(self.channel_layer.group_discard)(self.groupName, self.channel_name)



class AsyncChatApp(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected....")
        self.groupName=self.scope['url_route']['kwargs']['groupName']
        print("Group name is: ",self.groupName)

        await self.channel_layer.group_add(self.groupName, self.channel_name)
        await self.accept()
    
    async def receive_json(self, content, **kwargs):
        print('Message Receive from client...',content)
        print("type of the message is: ",type(content))

        message=content['msg']
        
        if self.scope['user'].is_authenticated:
        # Save the message into Database
            await database_sync_to_async(self.save_chat_message)(message)


            await self.channel_layer.group_send(
                self.groupName, 
                {
                    'type': 'chat.message',
                    'text': message
                }
            )
        else:
            await self.send_json({'msg':"login Required"})

    async def chat_message(self, event):
        message=event['text']
        await self.send_json({'msg':message})

        # await self.send_json({"msg":"message from server"})
        # await self.close(code=4321)       # Froce to close
        
    async def disconnect(self, close_code):
        print("Websocket Disconnect....",close_code)
        await self.channel_layer.group_discard(self.groupName, self.channel_name)

    def save_chat_message(self,message):
        group=  Group.objects.filter(name=self.groupName).first()
        if group:
            chat =  Chat(content=message, group=group)
        else:
            group=Group(name=self.groupName)
            group.save()
            chat = Chat(content=message, group=group)
        chat.save()
        