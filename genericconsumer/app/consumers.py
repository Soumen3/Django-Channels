

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket connected....")
        self.accept() # To accept the connection
        # self.close() # To reject the connection

    def receive(self, text_data=None, bytes_data=None):
        print("Message recieved from client...",text_data)
        self.send(text_data='Msg from server..')
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
        await self.send(text_data='Msg from server..')
        # await self.close(code=4123)   # To add a custom websocket error code

    async def disconnect(self, close_code):
        print("Websocket Disconnected...",close_code)