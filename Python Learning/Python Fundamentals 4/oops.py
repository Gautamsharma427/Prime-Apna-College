# oops stands for object oriented programming. It is the basis of modern day programming.
# It is done using classes and objects.
# Code written using oops is highly reusable.
# Programming using oops is optional but there are many problems which can be easily solved using oops.
# Object oriented programming is mapping real world objects with programming.
# Class is a blueprint for creating objects. It defines the properties and behaviors of the objects.
# Object is an instance of a class. It has its own state and behavior.
# you don't need to define same thing again and again.

# CLASS IS A BLUEPRINT FOR CREATING OBJECTS

class Student:
    # Properties are defined here
    subject = "Python"
    college = "ABC"
    year = "4th year"

    # __init__ method is called constructor and is called automatically when a instance of a class is created
    # a self is automatically given 1
    def __init__(self,name):
        print("This is present in init")
        print(self)
        self.name = name

#Object of Class student
student1 = Student("alice")
print(student1.name)

# we can access properties of object of class student using the dot operator
print(student1.college,student1.year,student1.subject)

# class can store properties as well as methods
#types of constructors in python
#1. default constructor
class Student1:
    def __init__(self):
        print("This is default constructor")
student2 = Student1()
#2. parameterized constructor
class Student2:
    def __init__(self,name):
        print("This is parameterized constructor")
        self.name = name
student3 = Student2("bob")
print(student3.name)

# attributes in python 
# types of attributes in python
#1. instance attributes
class Student3:
    def __init__(self,name):
        self.name = name
student4 = Student3("charlie")
print(student4.name)
#2. class attributes
class Student4:
    college = "XYZ" # class attribute
    
student5 = Student4()
print(student5.college)

#instance attributes can be accessed only using the object of the class while class attributes can be accessed using the class name as well as the object of the class
print(Student4.college) # accessing class attribute using class name
print(student5.college) # accessing class attribute using object of the class
print(student4.name) # accessing instance attribute using object of the class
# print(Student4.name) # this will give an error because name is an instance attribute and cannot be accessed using the class name
# instance attribute has higher priority than class attribute if both have same name 