import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# To achive the same thing we did using threading.Thread, lets use ThreadPoolExecutor

start_time = time.perf_counter()


def sleep(seconds: int | float) -> str:
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping {seconds} second(s)"


# creating thread pool executor
with ThreadPoolExecutor() as executor:
    f1 = executor.submit(sleep, 10)
    f2 = executor.submit(sleep, 10)

    print(f1.result())
    print(f2.result())


end_time = time.perf_counter()

print(f"Finished in {round(end_time - start_time, 2)} second(s)")


# --------------------------------------------------------------------------------------------------

start_time = time.perf_counter()


def sleep1(seconds: int | float) -> str:
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping {seconds} second(s)"


# creating thread pool executor
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(sleep1, 10) for _ in range(10)]

    # [print(future.result()) for future in futures]  # use this to get the results

    # or use as_completed() method as well
    for f in as_completed(futures):
        print(f.result())


end_time = time.perf_counter()

print(f"Finished in {round(end_time - start_time, 2)} second(s)")

# --------------------------------------------------------------------------------------------------

start_time = time.perf_counter()


def sleep2(seconds: int | float) -> str:
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done sleeping {seconds} second(s)"


# creating thread pool executor
with ThreadPoolExecutor() as executor:
    seconds = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    futures = [executor.submit(sleep2, second) for second in seconds]

    # [
    #     print(future.result()) for future in futures
    # ]  # use this to get the results (maintains the sequence)

    # or use as_completed() method as well
    for f in as_completed(futures):
        print(f.result())


end_time = time.perf_counter()

print(f"Finished in {round(end_time - start_time, 2)} second(s)")
