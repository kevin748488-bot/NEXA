import asyncio
from bleak import BleakScanner

async def escanear():
    dispositivos = await BleakScanner.discover()

    for d in dispositivos:
        print(d.name, d.address)

asyncio.run(escanear())
