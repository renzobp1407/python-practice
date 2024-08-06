# Lambda functions are functions that are almost solely used to get inputs and return outputs.
# That means we don't often use them to make actions.
# For example, the `print()` function is a function that performs an action. As such, it would not be suitable for lambda function.
# If we wanted a function that just divided two numbers, that might be suitable for a lambda function.

# That's because that function takes inputs, processes them, and returns outputs. And, it's a short, simple function. You'll see why that is relevant with this example.


# Basically in takes 2 inputs, makes a division (or operation) and returns the result 
divide = lambda x, y: x / y

#it equals to this
def divide(x, y):
    return x / y

lambda x, y: x / y # no name to the lambda and it will do their job but cannot use recursively

result = (lambda x, y: x + y)(15, 3) #not recomended approach, confusing
print(result)

#----------------------------------
#nomal function
def average(sequence):
  return sum(sequence) / len(sequence)


students = [
  {"name": "Rolf", "grades": (67, 90, 95, 100)},
  {"name": "Bob", "grades": (56, 78, 80, 90)},
  {"name": "Jen", "grades": (98, 90, 95, 99)},
  {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
  print(average(student["grades"]))

# it can be done like this

average2 = lambda sequence: sum(sequence) / len(sequence) #can be better scenarios

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average2(student["grades"]))




