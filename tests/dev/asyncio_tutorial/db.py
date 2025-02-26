import asyncio
from concurrent.futures import ThreadPoolExecutor


def run_debugger():
    import pdb

    pdb.set_trace()


async def random_task():
    await asyncio.sleep(2)
    print(1 + 1)


async def debuggable_task():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, run_debugger)

    await asyncio.sleep(1)


async def main():
    await asyncio.gather(random_task(), debuggable_task())


asyncio.run(main())
