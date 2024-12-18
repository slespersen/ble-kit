import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for device in devices:
        print(device.name)
        print(device.address)
        print(device.details)
        #print(device.metadata)
        #print(device.rssi)

asyncio.run(main())
