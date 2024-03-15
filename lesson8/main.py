import os
import time
import asyncio
from datetime import datetime

COEFF = 1


async def dish(num, prepare, wait):
    print(f"start {datetime.now().strftime('%HH:%MM:%SS')} "
          f"prepare dish {num} {prepare} min")
    time.sleep(COEFF * prepare)
    print(f"start {datetime.now().strftime('%HH:%MM:%SS')} "
          f"wait dish {num} {wait} min")
    await asyncio.sleep(COEFF * wait)
    print(f"start {datetime.now().strftime('%HH:%MM:%SS')} "
          f"dish {num} is ready")


async def main():
    tasks = [
        asyncio.create_task(dish(1, 2, 3)),
        asyncio.create_task(dish(2, 5, 10)),
        asyncio.create_task(dish(3, 3, 5))
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time.time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    delta = int((time.time() - t0) / COEFF)
    print(f"{datetime.now().strftime('%HH:%MM:%SS')} It took {delta} min")
