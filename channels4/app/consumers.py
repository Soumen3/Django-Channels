

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Connected")
        self.send({
            "type":"websocket.accept",
        })
        
    def websocket_receive(self, event):
        message = event['text']
        print(message)
        self.send({
            'type':'websocket.send',
            'text':' message send to client'
            })
        
    def websocket_disconnect(self,event):
        print('Disconnected')
        raise StopConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Connected")
        await self.send({
            "type":"websocket.accept",
        })
        
    async def websocket_receive(self, event):
        message = event['text']
        print(message)
        await self.send({
            'type':'websocket.send',
            'text':' message send to client from async'
            })
        
    async def websocket_disconnect(self,event):
        print('Disconnected')
        raise StopConsumer
