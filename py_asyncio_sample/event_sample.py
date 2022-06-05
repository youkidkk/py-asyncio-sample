import asyncio


async def wait_event(event: asyncio.Event):
    print("Task start.")
    await event.wait()
    print("Task end.")


async def main():
    event = asyncio.Event()
    task = asyncio.create_task(wait_event(event))
    await asyncio.sleep(5)
    event.set()
    await task


asyncio.run(main())
