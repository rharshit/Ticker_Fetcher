import asyncio

import websockets

from multiserver import Server

server = Server()


async def hello(port):
    uri = "ws://localhost:" + str(port)
    async with websockets.connect(uri) as websocket:
        print("Connected to port", port)
        while True:
            greeting = await websocket.recv()
            print(port, greeting)


port = server.get_port()
asyncio.get_event_loop().run_until_complete(hello(port))
