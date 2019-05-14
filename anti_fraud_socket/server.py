import os
import random
import asyncio
import websockets


WEBSOCKET_HOST = os.getenv('WEBSOCKET_HOST_SERVER', '127.0.0.1')
WEBSOCKET_PORT = os.getenv('WEBSOCKET_PORT', '50007')


def get_normalvariate_bytes(sequence_number, mu=0, sigma=1):
    yield ':'.join(
        map(str, (random.normalvariate(mu, sigma), sequence_number))
    ).encode()


async def normal_sender(websocket, path):
    sequence_number = 0
    while True:
        variate_with_sequence = get_normalvariate_bytes(sequence_number)
        await websocket.send(variate_with_sequence)
        sequence_number += 1
        await asyncio.sleep(4)


start_server = websockets.serve(normal_sender, WEBSOCKET_HOST, WEBSOCKET_PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
