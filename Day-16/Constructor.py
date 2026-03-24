# Day-16: Constructor Example

class Student:
    def __init__(self, name, age, course):
        # Constructor to initialize object properties
        self.name = name
        self.age = age
        self.course = course

# Creating object
s1 = Student("Rohan", 22, "MCA")

# Printing details
print("Name:", s1.name)
print("Age:", s1.age)
print("Course:", s1.course)