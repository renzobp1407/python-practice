

class Student:

  def __init__(self, new_name, new_grade):
    self.name = new_name  # this is a properties
    self.grades = new_grade

  def average(self): #this is a Method
    return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

#print(student_one.name)
#print(student_two.name)
#print(student_one.__class__)

# Self refers to the first object that we are modifing or acting

print(student_one.average())
# in reality, when you call only average() python knows that you ar calling  student_one = print(student_one.name) 
