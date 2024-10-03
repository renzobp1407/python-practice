from threading import Thread
import time
import random
import queue


counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # this waits until an item is available and locks the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter +  increment
        time.sleep(random.random())
        job_queue.put((f'New counter value {counter}', '-----------'))
        time.sleep(random.random())
        counter_queue.task_done() #this unlocks the queue
        
# printer_manager and increment_manager run continuosly because of the 'daemon' flag
Thread(target=increment_manager, daemon=True).start()
# the daemon is for endless use o the resource

def printer_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)
        job_queue.task_done()

Thread(target=printer_manager, daemon=True).start()

def increment_counter():
    counter_queue.put(1)
    time.sleep(random.random())
    
workers_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in workers_threads:
    time.sleep(random.random())
    thread.start()
    
for thread in workers_threads:
    thread.join() # wait fot it to finish

counter_queue.join() # wait for the counter_queue to be empty
job_queue.join() # wait for the job_queue to be empty