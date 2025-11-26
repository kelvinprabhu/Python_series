# import threading
# # threading is a module that allows for concurrent execution of code using threads.and it is used to improve the performance of I/O-bound tasks.
# import time

# def worker(number):
#     print(f"Worker {number} starting")
#     time.sleep(2)
#     print(f"Worker {number} finished")
# threads = []

# print(f"time before starting threads: {time.strftime('%X')}")
# for i in range(5):
#     thread = threading.Thread(target=worker, args=(i,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()

# print(f"time after finishing threads: {time.strftime('%X')}")

from threading import Lock,Thread
import time
lock = Lock()
counter = 0
def inc_counter():
    global counter
    for _ in range(100000):
        lock.acquire()
        counter += 1
        time.sleep(0.1)
        lock.release()
# The lock is used to ensure that only one thread can modify the counter variable at a time, preventing race conditions
if __name__ == "__main__":
    print("start value",counter)
    t1 = Thread(target=inc_counter,args=(counter,))
    t2 = Thread(target=inc_counter,args=(counter,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("end value",counter)

