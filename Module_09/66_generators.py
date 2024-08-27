"""
A generator in Python is a function that remembers the state it’s in, in between executions.

Let’s explain with an example. Imagine you wanted to build a list of 100 numbers, like this one:
"""

def hundred_numbers ():
    nums = []
    i = 0
    while i < 100:
        num.append()
        i+=1
    return nums    

print(hundred_numbers())    

# print([ x * 2 for x in hundred_numbers() ])

"""
We could use list comprehension for this and the `range()` function, but for now let’s assume that this is a cool way of doing it. We construct a list, fill it with the first 100 numbers, and then return them.

We now have 100 numbers in a list. The entire list is in your computer’s RAM memory, taking up an admittedly small amount of space.

If we wanted 10,000,000 numbers, the list would be substantially bigger. As you grow the number, the amount of memory taken up by the list also grows.

A generator is used to circumvent this problem. Instead of having a list, the first time you run the function you would get the first number (`0`). The second time you run the function you’d get `1`. Then `2`, and so on.

You have to run the function every time you want a new number, that’s why it’s called a “generator”. It generates numbers (or indeed strings, or anything else you want to generate).
"""

# generator function
def hundred_numbers():
  num = 0
  while num < 100:
    yield num
    num += 1

# if we print like normal, it will print a generator object:
# <generator object hunderd?number at 0x7fdgrj45jv8>
# yield num turns it to a python object

g = hundred_numbers()
print(next(g)) # print 0
print(next(g)) # print 1
print(next(g)) # print 2

# next is a build in function to use with generators
# the idea is to know where the next generation of number or string will use it and use the precise value or stop it when need it

# range work similar to yield but it cannot use next() function

my_range_obj = range(10)
next(my_range_obj) # will print error
print(my_range_obj) # will print "range (0, 10)"
print(my_range_obj.__repr__())


# the list function can turn a generator into a list

print(list(g)) # will print from 2 to 100, missing the 0 and 1 with the yield function because he remembers where it stoped

"""
The `yield` keyword is very much like a `return`, in that it gives the value back to the caller and returns execution control to them (show this with example run). However, the next time you run the function, execution continues from the very next line inside the function, instead of from the top.

We could re-write the function as a list comprehension:
"""

hundred_numbers = [n for n in range(100)]



"""
Or indeed as a generator comprehension. This is essentially the same thing, including the `yield` statement.
"""

hundred_numbers = (n for n in range(100))
print(next(hundred_numbers))
print(next(hundred_numbers))

print(list(hundred_numbers))

"""
Notice that when we do the code snippet above, `next()` runs the function once up until the `yield` (which would give you the first value). The following `next()` runs it again, which gives you the second value. Then, turning it into a list continues and builds a list from the remaining values (that’s only 98 values left).

A few sections ago I printed out `range(10)` and it was a strange `range(0, 10)` thing. That’s a generator object!
"""