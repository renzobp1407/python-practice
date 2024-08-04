from _typeshed import SupportsDivMod


def greet():
  print("Hello")


greet  #Valid python syntax but no print

Hello = greet

hello()

#firts class function refers to a function that takes no arguments and returns no value


def average(seq):
  return sum(seq) / len(seq)


avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
  name = student["name"]
  grades = student["grades"]

  print(f"Student: {name}")
  operation = input("Enter 'average', 'total', or 'top': ")

  if operation == "average":
    print(avg(grades))
  elif operation == "total":
    print(total(grades))
  elif operation == "top":
    print(top(grades))

# New function more simpler
# Using diccionaries to store the operations and asociation

operations = {
    "average": avg,
    "total": total,
    "top": top
}

for student in students:
  name = student["name"]
  grades = student["grades"]

  print(f"Student: {name}")
  operation = input("Enter 'average', 'total', or 'top': ")

  operation_function =  operations[operation]
  print(operation_function(grades))

#With a Dicctionary we can get an error when we search to a key that dosen't exist (different input)

#it can be more complicated and not recomended


operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
   # "total": sum,
   # this is the optimized version
    "top": lambda seq: max(seq)
}

