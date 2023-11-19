# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EngineConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process the received message from the Go app
        data = json.loads(text_data)
        # Perform actions based on the received data
        # Send a response if needed
        await self.send(text_data=json.dumps({'message': 'Consumer response message'}))
