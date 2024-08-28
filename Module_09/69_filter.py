"""
Now that we’ve got our generators, iterators, and iterables out of the way, we can start with some fun built-in functions.

Let’s start with `filter()`.

The `filter()` function is a built-in function in Python that you can call from any file or program.

It takes two arguments:

* A function; and
* An iterable (now we know what these are!)

It goes like this:
"""
# Initial function

# def starts_with_r(friend):
#     return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
# start_with_r = filter(start_with_r, friends) # arg 1: function that returns True/false
start_with_r = filter(lambda x: x.startswith('R'), friends) 
# another_starts_with_r = (f for f in friends if f.startswith('R')) # the same as the lambda
print(start_with_r)  # generator!

print(list(start_with_r))
print(list(start_with_r))  # won't work, the generator has already gone through all its elements

# remember that the Iterator remembers the last value, in this case filter()

# filter returns an iterator