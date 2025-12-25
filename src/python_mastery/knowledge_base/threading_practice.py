import threading
import time

# Threading concepts

# What is thread?
# A thread is a smallest unit of execution in a process that does a specific task

# Example

# execution in sync manner (everything runs in main thread)
start_time = time.perf_counter()


def sleep():
    print("Sleeping for a second")
    time.sleep(1)
    print("Done sleeping")


# calling sleep() for 3 times
sleep()
sleep()
sleep()

end_time = time.perf_counter()

print(f"Time taken to complete tasks in sync manner: {round(end_time - start_time, 2)} second(s)")

# now lets achieve the same in async manner using Thread

start_time = time.perf_counter()


def sleep1():
    print("Sleeping for a second")
    time.sleep(1)
    print("Done sleeping")


# create thread and assingn task
t1 = threading.Thread(target=sleep1)
t2 = threading.Thread(target=sleep1)
t3 = threading.Thread(target=sleep1)

# now sart the threads
t1.start()
t2.start()
t3.start()

# wait for threads to finish the tasks
t1.join()
t2.join()
t3.join()

end_time = time.perf_counter()

print(f"Time taken to complete tasks in async manner: {round(end_time - start_time, 2)} second(s)")


# say we are calling some function 10 times, careating and managing threads manually may become big code. we can use for loop for it

start_time = time.perf_counter()


def sleep2():
    print("Sleeping for second")
    time.sleep(1)
    print("Sleeping finished")


# if I want to call this 10 times in each thread, we can simply use for loop
threads: list[threading.Thread] = []
for _ in range(10):
    thread = threading.Thread(target=sleep2)
    thread.start()
    threads.append(thread)

# wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.perf_counter()

print(
    f"Time taken to complete tasks in async manner with loop: {round(end_time - start_time, 2)} second(s)"
)
