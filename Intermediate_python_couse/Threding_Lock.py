# Threading in Python is the classic story of many cooks, one kitchen. The “kitchen” is your shared data.
#  The “cooks” are your threads. Life goes fine until two cooks try to chop the same carrot at the same time — then you get a mess. Locks are the kitchen rules preventing that chaos.
# Without locks, threads can interfere with each other when accessing shared data, leading to unpredictable results.
from threading import Lock,Thread
import time
counter = 0
def inc_counter():
    global counter
    # counter += 1
    for _ in range(10000000):
        counter += 1
threads = []
for _ in range(5):
    t = Thread(target=inc_counter)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)
# If two threads overlap between steps 1 and 3, one thread overwrites the other’s work. That’s a race condition.
counter_l = 0
lock = Lock()
def inc_counter_l():
    global counter_l
    # counter += 1
    for _ in range(10000000):
        with lock:
            counter_l += 1
threads_l = []
for _ in range(5):
    t = Thread(target=inc_counter_l)
    threads_l.append(t)
    t.start()

for t in threads_l:
    t.join()
print("Final counter value with lock:", counter_l)