import pprint

import websocket


def on_message(wsapp, message):
    pprint.pprint(message)
    print()
    print()
    print()
    print()


# wsapp = websocket.WebSocketApp("wss://stream.meetup.com/2/rsvps", on_message=on_message)
wsapp = websocket.WebSocketApp("ws://localhost:8765", on_message=on_message)
wsapp.run_forever()
