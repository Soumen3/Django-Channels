

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket connected....")
        self.accept() # To accept the connection
        # self.close() # To reject the connection

    def receive(self, text_data=None, bytes_data=None):
        print("Message recieved from client...",text_data)
        self.send(text_data='Msg from server..')
        for i in range(10):
            self.send(text_data=str(i))
            sleep(1)
        # self.close(code=4123)   # To add a custom websocket error code

    def disconnect(self, close_code):
        print("Websocket Disconnected...",close_code)




class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket connected....")
        await self.accept() # To accept the connection
        # await self.close() # To reject the connection

    async def receive(self, text_data=None, bytes_data=None):
        print("Message recieved from client...",text_data)
        await self.send(text_data='Msg from server....')
        for i in range(10):
            await self.send(text_data=str(i))
            await asyncio.sleep(1)
        # await self.close(code=4123)   # To add a custom websocket error code

    async def disconnect(self, close_code):
        print("Websocket Disconnected...",close_code)