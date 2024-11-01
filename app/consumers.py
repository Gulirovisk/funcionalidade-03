# sua_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AnimalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Enviar uma resposta de volta
        await self.send(text_data=json.dumps({
            'message': f"Recebido: {message}"
        }))
