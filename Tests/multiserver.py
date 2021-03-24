import asyncio
from datetime import datetime

import websockets

server_start_port = 8100
server_end_port = 8200


class Server:
    def __init__(self):
        self.servers = {}

    async def hello(self, websocket, path):
        try:
            while True:
                print()
                print("Servers")
                print(self.servers)
                now = datetime.now()
                message = now.strftime("%H:%M:%S")
                await websocket.send(message)
                await asyncio.sleep(1)
        except Exception as e:
            print(e)
        finally:
            for port in self.servers.keys():
                if self.servers.get(port) == websocket:
                    print("Stopping server at port {}".format(port))
                    del self.servers[port]

    def get_port(self):
        for port in range(server_start_port, server_end_port):
            print(self.servers)
            if port in self.servers.keys():
                print("Port {} in server list".format(port))
                continue
            else:
                # self.servers[port] = None
                try:
                    websocket = websockets.serve(self.hello, "localhost", port)
                    asyncio.get_event_loop().run_until_complete(websocket)
                    self.servers[port] = websocket
                    print("Starting server at port {}".format(port))
                except Exception as e:
                    print("Skipping port {}".format(port))
                    continue
                return port
        return 0

    def add_port(self, port):
        if port < server_start_port or port > server_end_port:
            return False
        elif port in self.servers.keys():
            return False
        else:
            self.servers[port] = websockets.serve(self.hello, "localhost", port)
            asyncio.get_event_loop().run_until_complete(self.servers[port])
            print("Starting server at port {}".format(port))
            return True

    # async def init(self):
    #     self.initialized = True
    #     asyncio.get_event_loop().run_forever()
