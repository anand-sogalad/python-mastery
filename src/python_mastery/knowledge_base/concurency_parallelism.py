import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from functools import wraps
from multiprocessing import Process
from threading import Thread


def timer(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = round(end_time - start_time, 2)
        print(f"Total time taken to execute {total_time} second(s)")
        return result

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = round(end_time - start_time, 2)
        print(f"Total time taken to execute {total_time} second(s)")
        return result

    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper


def sleep(seconds=10):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    print(f"Sleeping completed for {seconds} second(s)")


async def sleep_async(seconds=10):
    print(f"Sleeping for {seconds} second(s)")
    await asyncio.sleep(seconds)
    print(f"Sleeping completed for {seconds} second(s)")


@timer
def execute_sync():
    for _ in range(10):
        sleep()


@timer
def execute_with_thread():
    # create thread for each task manually
    t1 = Thread(target=sleep)
    t2 = Thread(target=sleep)
    t3 = Thread(target=sleep)
    t4 = Thread(target=sleep)
    t5 = Thread(target=sleep)
    t6 = Thread(target=sleep)
    t7 = Thread(target=sleep)
    t8 = Thread(target=sleep)
    t9 = Thread(target=sleep)
    t10 = Thread(target=sleep)

    # start each thread manually
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    # wait for thread to finish the task
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()


@timer
def execute_with_thread_loop():
    threads: list[Thread] = []
    for _ in range(10):
        thread = Thread(target=sleep)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


@timer
def execute_with_thread_pool_submit():
    with ThreadPoolExecutor() as tpe:
        futures = [tpe.submit(sleep) for _ in range(10)]
        for future in as_completed(futures):
            print(future.result())


@timer
def execute_with_thread_pool_map():
    with ThreadPoolExecutor() as tpe:
        results = tpe.map(sleep, [10 for _ in range(10)])
        for result in results:
            print(result)


@timer
async def execute_sleep_async():
    results = await asyncio.gather(*[sleep_async() for _ in range(10)])
    return results


if __name__ == "__main__":
    execute_sync()
    execute_with_thread()
    execute_with_thread_loop()
    execute_with_thread_pool_submit()
    execute_with_thread_pool_map()
    asyncio.run(execute_sleep_async())
