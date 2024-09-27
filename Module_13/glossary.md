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
