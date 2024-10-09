# Glossary

Throughout the section we'll learn more about what these terms mean, but it can be helpful to have a short glossary of terms just in case you want to come back and remind yourself.

- Synchronous: actions that happen one after another.Programming as we've seen it until now is synchronous, because each line executes after the previous one.
- Asynchronous: actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").
- Concurrency: The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.
- Parallelism: Running two or more things at the same time.
Thread: A line of code execution that can run in one of your computer's cores.
- Process: One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).
GIL: A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.

## Dinnig Philosophers problem

- limited resources
- waiting the people
- the waiter is a must to resolve the problem
- we can't have 3 phlosophers eating at once

## procees and threads

- Core a unit can perform math operations
- each proceso have a # of cores
- waiting threads there aren't on the procesor core
- Thread is a line of code execution
- one thread can run in one core at a time
- procesess: some resources set aside by the operationg system
- the process is what manages all the resources that it nees in order to run 


## Pyhton GIL (The Global Interpreter Lock)

- you cannot run two threads in one process at the same time
- each process in pyhton creates a Key Resource
- when a thread is runnig, it must acquire that resource since theres's only one of that, only one thread can run in a process at once

## Multiple Pythons

you can, however, launch multiple pythons proces
- each process in python creates it's own GIL
- Each process creates one thread but they cannot easily share data (e.g Have the same variables)

## whats the point of thread in python

R// reduce waiting time

- do 2 things at the same time

- single thread: mathematical calculation and user input
or user input and mathematical calculation 

Cooperative multitasking (but only one thread can run at a time)

- we can ask the user the input and when he is typing the mathematical process executes taking the GIL (and releasing), and when the user input the string, it wil go back to the user process again and continues the math process

## dont kill the thread

- don't kill the thread before it releases GIL, it can do an execution error on the thread list, this is called *Deadlock*

## Multiprocessing in Windows or ARM Macs

In the lecture, Windows or ARM Mac (M1, M2, etc) users might encounter a small issue.

Due to the way these systems work you must make sure that the code that starts a process is surrounded by if __name__ == "__main__".

Otherwise when we start new processes, those processes automatically start new processes, and those start new ones, and so on. Python will not allow this to happen, and as protection it requires the above if statement.

Join() = espera que temine el proceso para empezar el que sigue

atomic operation = is a process that cannot be interrupted in the middle of it

adding random to multithreaded codes is called fuzzying

Priming the generator: 
g = greet()
g.send(none) # priming the generator

Co routine: they can take data and can be suspended
