from queue import Queue
from threading import Thread
import time

q = Queue()
# Queue is FIFO (First In First Out)
for i in range(10):
    q.put(i)
    # 10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0
# print(q.get())
# print(q.get())
# q.task_done()
q.join()
# Blocks until all items in the queue have been gotten and processed.
# print(q.qsize())  # 8
# print(q.empty())  # False
def worker():
    while True:
        item = q.get()
        print(f'Processing item: {item}')
        print({'thread': Thread.name})
        time.sleep(1)  # Simulate a time-consuming task
        q.task_done()
threats = []
for i in range(10):
    threats.append(Thread(target=worker))
    threats.daemon = True # Daemon threads run in the background and do not block the main program from exiting.
    threats.start()