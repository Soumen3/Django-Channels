# Topic - Consumer

from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    """This handler is called when client initialy opens a connection and is about to finish the websocket handshake"""
    def websocket_connect(self, event):
        print('Websocket Connected...')
    
    """This handler is called when data received from client"""
    def websocket_receive(self,event):
        print('WebSocket Received...')

    """This handler is called when either connection to the client is lost, either from the client closing the connection, the server       closing the connection, or lose the socket"""
    def websocket_disconnect(self,event):
        print('WebSocket Disconnected...')

    

class MySyncConsumer(AsyncConsumer):
    """This handler is called when client initialy opens a connection and is about to finish the websocket handshake"""
    async def websocket_connect(self, event):
        print('Websocket Connected...')
    
    """This handler is called when data received from client"""
    async def websocket_receive(self,event):
        print('WebSocket Received...')

    """This handler is called when either connection to the client is lost, either from the client closing the connection, the server       closing the connection, or lose the socket"""
    async def websocket_disconnect(self,event):
        print('WebSocket Disconnected...')

    