"""
The `map()` function is used to take an iterable and output a new iterable where each element has been modified according to some function.

For example, this `map()`:
"""

friends = ["Rolf", "Charlie", "Anna"]
friends_lower = map(lambda x: x.lower(), friends)

print(friends_lower)

print(list(friends_lower))

"""
This of course could be written (arguably better / more pythonically) as a list or generator comprehension:
"""

friends_lower = [friend.lower() for friend in friends]

friends_lower = (friend.lower() for friend in friends)

"""
However there is something to be said for using `map()` and *not* creating the useless `friend` variable that you need to create for list comprehension.

I still think list comprehension is more pythonic and more readable.

However, if you already have the function you’re going to use defined, `map()` may not be such bad a choice. Here’s an example:
"""


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"])


# imagine these users are coming from a database...

users = [
    {"username": "rolf", "password": "123"},
    {"username": "tecladoisawesome", "password": "youaretoo"},
]

user_objects = map(User.from_dict, users)

"""
The option of using a list comprehension is slightly uglier, I feel:
"""

user_objects = [User.from_dict(u) for u in users]

"""
Although of course, using dictionary unpacking everything would be made much simpler… More on that in a coming section!
"""

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))