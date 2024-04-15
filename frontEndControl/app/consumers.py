
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
import time
import asyncio, json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connected...")
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        message=event['text']
        print("Message from client: ",message)
        for i in range(10):
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({'msg':f'{i} message send to client'})   # send object as a string, because the text onle accept str object
            })
            time.sleep(1)
        
    def websocket_disconnect(self, event):
        print('Disconnected...')
        raise StopConsumer
    


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected...")
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        message=event['text']
        print(message)
        for i in range(10):
            await self.send({
                'type': 'websocket.send',
                'text': f'{i} message send to client'
            })
            await asyncio.sleep(1)
        
    async def websocket_disconnect(self, event):
        print('Disconnected...')
        raise StopConsumer