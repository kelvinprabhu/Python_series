from threading import Thread
from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import Futures
import time
def task(n):
    print(f"Task {n} starting")
    time.sleep(2)
    return print(f"Task {n} finished")
    # return n * 2
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in futures:
        print(future.result())
# The ThreadPoolExecutor manages a pool of threads, allowing you to run multiple tasks concurrently without manually creating and managing individual threads.
# Benefits:

# Reuses threads → less overhead

# Automatically manages starting, joining, scheduling

# Cleaner API with futures

# Built-in exception handling

# Scales nicely for I/O-bound tasks
