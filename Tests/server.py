import asyncio

import websockets


async def hello(websocket, path):
    print(path)
    while True:
        message = "Test"
        await websocket.send(message)
        await asyncio.sleep(1)


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
