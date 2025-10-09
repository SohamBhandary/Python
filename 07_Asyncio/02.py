import asyncio
import time

async def brew(name):
    print(f"Brewing:{name}")
    time.sleep(2)
    print(f"Finished:{name}")

async def main():
    await asyncio.gather(brew("masla"),
    brew("ginger"))

asyncio.run(main())