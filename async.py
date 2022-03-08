import asyncio
import uvloop


async def fetch_data():
    print("start fetching data ...")
    await asyncio.sleep(2)
    print("fetching data is done.")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    # task1 = asyncio.create_task(fetch_data())
    # task2 = asyncio.create_task(print_numbers())
    # res = [await task1, await task2]

    res = await asyncio.gather(fetch_data(), print_numbers())
    print(res)


uvloop.install()
asyncio.run(main())
