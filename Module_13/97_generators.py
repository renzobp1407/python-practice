def countdown(n):
    while n > 0:
        yield n
        n -=1


task = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        task.append(task)
    except StopIteration:
        print('task finished')    
