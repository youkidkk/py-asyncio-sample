import asyncio

sem = asyncio.Semaphore(3)


async def task(name: str):
    async with sem:
        print(f"{name} start!")
        await asyncio.sleep(3)
        print(f"{name} end!!!")


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(task(f"Task{i}")))
    for t in tasks:
        await t


asyncio.run(main())
