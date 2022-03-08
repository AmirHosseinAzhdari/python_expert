import time
import multiprocessing as mp


async def fetch_data():
    print("start_fetching data ...")
    a = 0
    t1 = time.time()
    for i in range(100):
        for j in range(400):
            for h in range(6000):
                a += 1
    print(time.time() - t1)
    # await asyncio.sleep(2)
    print(a)
    print("fetching data is done.")
    return {"data": a}
