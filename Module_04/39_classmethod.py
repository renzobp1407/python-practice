
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


"""
When we create a new object from the `Student` class and we call a method, we are automagically passing in the `self` parameter:
"""

rolf = Student("Rolf", "MIT")

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())

"""
This is identical to that last line:
"""

print(Student.average(rolf))

"""
When we do `object.method()`, Python is in the background calling `Class.method(object)`, so that `self` is always the object that called the method.

Indeed, if we were to have two objects:
"""

rolf = Student("Rolf", "MIT")
anne = Student("Anne", "Cambridge")

rolf.marks.append(78)
rolf.marks.append(99)

anne.marks.append(34)
anne.marks.append(56)

print(rolf.average())
print(anne.average())

"""
In the first case, `self` would be the `rolf` object, and in the second case `self` would be the `anne` object.

Notice that this knowledge now lets us do some very weird stuff (not recommended, as it’ll likely break things):
"""

Student.average(
    "hello"
)  # self is now 'hello', comment this out to run the rest of the file.