import time
from threading import Thread

####### SINGLE THREAD

def ask_user():
    start = time.time()
    user_input = input('enter your name: ')
    greet = f'Hello, [user_input]'
    print(greet)
    print('ask_user: ', time.time() - start)
    
def complex_calculation():
    print('Started calculating...')
    start = time.time()
    [x**2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - start)
    
# wih a single thread, we can do one at a time

start = time.time()
ask_user()
complex_calculation()
print('single thread total time: ', time.time() - start, '\n\n')

####### SINGLE THREAD

# with two threads, we can do them both at once
thread = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread.start()
thread2.start()

thread.join()
thread2.join()

print('two thread total time: ', time.time() - start)