import asyncio

async def brew_chai():
    print("Brew")
    await asyncio.sleep(2)
    print("finished")

asyncio.run(brew_chai())