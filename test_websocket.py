import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/animal/"  # A URL do seu WebSocket
    try:
        async with websockets.connect(uri) as websocket:
            print("Conectado ao WebSocket")
            await websocket.send(json.dumps({'message': 'Olá, servidor!'}))
            response = await websocket.recv()
            print(f"Resposta do servidor: {response}")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())
