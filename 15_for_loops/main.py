friends = ["Rolf", "Anne", "Charlie"]

#DEclared a new variable friend for each element of the list
for friend in friends:
    print(friend)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#You can user alternative underscore to replate index
# for _ in elements:
for index in elements: 
    print("hello, world!")

#You can use range
for index in range(10): 
    print("hello, world!") 

#You can add more numbers to go from one to another
for index in range(5, 10): 
    print(index) 

#You can add a 3rd number to print 3 by 3
for index in range(2, 20, 3):
    print(index) 

students = [
  {"name": "Rolf", "grade": 90},
  {"name": "Bob", "grade": 78},
  {"name": "Jen", "grade": 100},
  {"name": "Anne", "grade": 80},
]

for student in students:
  name = student["name"]
  grade = student["grade"]
  print(f"{name} has a grade of {grade}.")

