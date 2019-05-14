import os
import asyncio
import websockets
import statistics
import datetime


WEBSOCKET_HOST_CLIENT = os.getenv('WEBSOCKET_HOST_CLIENT', '127.0.0.1')
WEBSOCKET_PORT = os.getenv('WEBSOCKET_PORT', '50007')
DJANGO_HOST = os.getenv('DJANGO_HOST', '127.0.0.1')
DJANGO_PORT = os.getenv('DJANGO_PORT', '8000')

WEBSOCKET_URL = f'ws://{WEBSOCKET_HOST_CLIENT}:{WEBSOCKET_PORT}'
DJANGO_WEBSOCKET_URL = f'ws://{DJANGO_HOST}:{DJANGO_PORT}/ws/notification/'

DEVIATION_LIMIT = 2


async def send_message(websocket_url: str, value: float, sequence_number: int):
    async with websockets.connect(websocket_url) as django_socket:
        await django_socket.send(
            f'{datetime.datetime.now()} | {sequence_number} | {value}')
        await django_socket.close()


async def proxy():
    async with websockets.connect(WEBSOCKET_URL) as websocket:
        standard_deviation = statistics.stdev((0, 1))
        while True:
            data = await websocket.recv()
            try:
                value, sequence_number = data.decode().split(':')
                value, sequence_number = float(value), int(sequence_number)
            except ValueError:
                value = None
            if value and abs(value) / standard_deviation > DEVIATION_LIMIT:
                await send_message(
                    DJANGO_WEBSOCKET_URL, value, sequence_number)


asyncio.get_event_loop().run_until_complete(proxy())
