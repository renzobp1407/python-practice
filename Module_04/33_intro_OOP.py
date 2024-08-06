my_student = {'name': 'Rolf Smith', 'grades': [70, 88, 90, 99]}


def average_grade(student):
  return sum(student['grades']) / len(student['grades'])


print(average_grade(my_student))

# the problem with the function is that not living with the student but is tightly coupled to that student

# the function is not flexible, if we want to add more student, we need to change the function

# we have to use Objects and Classes
#  __init__() = Dunder function, dunder Init
#  self = this is a blank object


class Student:

  def __init__(self, new_name, new_grade):
    self.name = new_name  #creating a variable inside the object
    self.grades = new_grade

  def average(self):
    return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.name)
print(student_two.name)
print(student_one.__class__)
