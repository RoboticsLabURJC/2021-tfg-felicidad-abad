#!/usr/bin/env python
## Client que nos pide un nombre, lo envía y después imprime el saludo
## recibido del server, ejemplo sacado de: https://websockets.readthedocs.io/en/stable/

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

asyncio.run(hello())
