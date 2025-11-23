import threading
# threading is a module that allows for concurrent execution of code using threads.and it is used to improve the performance of I/O-bound tasks.
import time

def worker(number):
    print(f"Worker {number} starting")
    time.sleep(2)
    print(f"Worker {number} finished")
threads = []

print(f"time before starting threads: {time.strftime('%X')}")
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print(f"time after finishing threads: {time.strftime('%X')}")

