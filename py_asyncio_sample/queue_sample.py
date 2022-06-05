import asyncio
import random


async def worker(name: str, queue: asyncio.Queue):
    while True:
        text = await queue.get()
        print(f"{name}: {text} start.")
        await asyncio.sleep(random.randint(3, 10))
        print(f"{name}: {text} end.")


async def main():
    queue_maxsize = 5
    queue = asyncio.Queue(maxsize=queue_maxsize)

    workers = []
    for i in range(1, 4):
        workers.append(asyncio.create_task(worker(f"Worker{i}", queue)))

    count = 1
    while True:
        await asyncio.sleep(1)
        if queue.full():
            print("The queue is full.")
            continue
        task_name = f"Task{count}"
        queue.put_nowait(task_name)
        count += 1
        print(f"{task_name} enqueue. ({queue.qsize()}/{queue_maxsize})")


asyncio.run(main())
