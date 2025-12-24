import threading
import time
from concurrent.futures import ThreadPoolExecutor

# What is thread?
# A thread is smallest unit of execution in a process that does specific task


def square(data: list[int]) -> list[int]:
    return [x**2 for x in data]


if __name__ == "__main__":
    chunks = range(1, 10000000), range(10000000, 0, -1)

    # using threading.Thread
    st = time.perf_counter()
    threads: list[threading.Thread] = []
    for chunk in chunks:
        t = threading.Thread(target=square, args=(chunk,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print(f"Total time: {time.perf_counter() - st}")

    # using thread pool executor
    st = time.perf_counter()
    with ThreadPoolExecutor(max_workers=len(chunks)) as worker:
        t = worker.map(square, chunks)
    print(f"Total time: {time.perf_counter() - st}")
