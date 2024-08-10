class Student:

  def __init__(self, name, school):
    self.name = name  # this is a properties
    self.grades = school
    self.marks = []

  def average(self): #this is a Method
    return sum(self.marks) / len(self.marks)

  # duplicate student
class WorkingStudent:

  def __init__(self, name, school, salary):
    self.name = name  # this is a properties
    self.grades = school
    self.marks = []
    self.salary = salary

  def average(self): #this is a Method
    return sum(self.marks) / len(self.marks)  

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary) 

# Implement Inheritance, is a exact copy of the student with new values added

# Working Student is a child of Student
class WorkingStudent2(Student): 
  def __init__(self, name, school, salary):
    super().__init__(name, school)
    self.salary = salary
  @property 
  def weekly_salary(self): #this is a Method
    return self.salary * 37.5      

rolf2 = WorkingStudent2('Rolf', 'MIT', 15.50)


print(rolf2.weekly_salary) 
# if we print this way, it's going to print a bound method without a decorator, 
#exaclty the definition of the metohd

# the property decorator is recomended to use only when there are going to calculate values from the object's
# properties







