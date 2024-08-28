class firstHundredGenerator:
  def __init__(self):
      self.number = 0

  def __next__(self):  
      if self.number < 100:
          current = self.number
          self.number += 1
          return current
      else: 
          raise StopIteration()

# the function generates 1 by 1 every time we call it instead we run every time the class

# all objects that hace __next__ dunder methods are called Iterators

# raise StopIteratin() it's stops the current for in de function of the class



my_gen = firstHundredGenerator()
print(my_gen.number) # 0
my_gen.__next__() 
print(my_gen.number) # 1
next(my_gen)
print(my_gen.number) # 2

# not all generators have to be iterators, this is important to undertand

"""
Notice how the object, with its property, remembers what the value of `self.number` is at all points in time.

This object is called in Python a generator because every time the next number is available not because it’s in a sequence, but because it is generated from its current state (in this case, by adding 1 to `self.number`).

All objects that have this `__next__` method are called iterators. All generators are iterators, but not the other way round.

For example, you could have an iterator on which you can call `next()`, but that doesn’t generate its values. Instead, it could take them from a list or from a database.

*Important*: iterators are objects which have a `__next__` method.

Here’s an example of an iterator which is not a generator:
"""

class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0
    
    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()

"""
As you can see it’s returning numbers that are not being generated; instead they’re being returned from a list.

If we run this code though, we will get an error:

"""

sum(FirstHundredGenerator())  # comment this line out to run the rest of the file.

"""
Similarly if we run this code:
"""

for i in FirstHundredGenerator():
    print(i)

"""
And that’s because in Python, an `iterator` and an `iterable` are different things. You can iterate over an `iterable`. The iterator is used to get the next value (either from a sequence or generated values).

> You can iterate over iterables, not over iterators.
"""            