# what is a process?
# A process is a running instance of a program with its its own memory


import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Process


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = round(time.perf_counter() - start_time, 2)
        print(f"Total time taken to execute {func.__name__} is {total_time} second(s)")
        return result

    return wrapper


def constant_sleep():
    print("sleeping for 5 seconds")
    time.sleep(5)
    print("Completed sleeping for 5 seconds")


def dynamic_sleep(seconds: int):
    print(f"sleeping for {seconds} seconds")
    time.sleep(5)
    print(f"Completed sleeping for {seconds} seconds")


@timer
def normal_constant_time():
    for _ in range(10):
        constant_sleep()


@timer
def normal_dynamic_time():
    seconds = [5, 4, 3, 2, 1]
    for second in seconds:
        dynamic_sleep(second)


@timer
def using_process_constant_1():
    processes: list[Process] = []
    for _ in range(10):
        process = Process(target=constant_sleep)
        process.start()
        processes.append(process)
    for process in processes:
        process.join()


@timer
def using_process_constant_2():
    with ProcessPoolExecutor() as executor:
        [executor.submit(constant_sleep) for _ in range(10)]


@timer
def using_process_dynamic_1():
    with ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        [executor.submit(dynamic_sleep, second) for second in seconds]


@timer
def using_process_dynamic_2():
    with ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        executor.map(dynamic_sleep, seconds)


if __name__ == "__main__":
    normal_constant_time()
    normal_dynamic_time()
    using_process_constant_1()
    using_process_constant_2()
    using_process_dynamic_1()
    using_process_dynamic_2()
