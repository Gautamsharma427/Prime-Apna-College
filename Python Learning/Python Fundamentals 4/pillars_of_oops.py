# Encaptulation: wrapping data and functions into one unit
# Data hiding is when we hide very sensitive data of our object in our class from user.
#   for example if we want to make a class about bank account which could contain various informatins like account id, balance, name, PIN etc.
#   in this example the balance and PIN are private variables which cannot be accessed outside the class as accidental change in these variables can cause problems. So We can make it private and only accessable inside the class by other class methods.

# example
class Bank_Account:
    def __init__(self,name,balance,pin):
        # Here Name is a PUBLIC Attribute 
        self.name = name
        
        # but for example let's say we want to make two private attributes of Balance and PIN then:
        self._balance = balance #we would include a underscore in front of the attribute name to make it a Protected attribute.
        self.__PIN = pin # we would include two underscores in front of the attribute name to make it a private attribute.
        # --Getters and Setters : Getters are the functions used to get the value of the private variable. Setters are  the variables used to set the values of Private Variables--
        # if we want to access the private attribute then we'll need to create a function in the class and then use that function outside the class to get the value of the private attribute
        
    # creating a Getter for Private Attribute __PIN:
    def get_PIN(self):
        return(self.__PIN)
    # creating a getter for Private attribute __PIN:
    def set_PIN(self,new_value):
        self.__PIN = new_value
Sourav = Bank_Account("Saurav Kumar", 13_500, 1111)

print(Sourav.name)
print(Sourav._balance) # it still stays accessible outside the class but it is not recommended to access the protected attributes by convention. It stays accessible in python because in python these rules are not enforced they are just present.
# print(Sourav.__PIN)#would return a error as it belongs to a private attribute and can't be accessed outside a class.
# We'll use the function we created in the class to access the value of the PIN:
print(f"PIN: {Sourav.get_PIN()}")
Sourav.set_PIN(1991) #using the setter function to update the value of the PIN attribute 
print(f"Updated PIN: {Sourav.get_PIN()}") # new PIN is updated to 1991

# but still as i already told that python doesn't enforce the rules so we can access our private variables in a different way too outside the class:
print(Sourav._Bank_Account__PIN) # here we printed the value of the private variable so easily but we don't do this because if we did this then there wouldn't be any point of encaptulation or data-hiding




#================================================================================================================================================================================







# 2. Inheritance: Reusing Attributes and methods from a parent class in a child class.
# parent class is the class whose properties are being inherited
# child class is the class which inherits the properties of the parent class
class Employee:
    start_time = "9:00 AM"
    end_time = "5:00 PM"

class Teacher(Employee):# Teacher inherits properties and methods of the class employee
    def __init__(self,subject):
        self.subject = subject
class Admin(Employee): # Admin inherits properties and methods of the class employee 
    def __init__(self,title):
        self.title = title
# in above example the parent class Employee has two child classes Teacher and Admin which can access all its properties
Ram = Teacher("Maths")
print(Ram.start_time,Ram.end_time,Ram.subject) #would acceszs start time and end time from the employee class and subject from the Teacher class

# A PROTECTED VARIABLE IS ACCESSIBLE IN A CHILD CLASS BUT A PROTECTED VARIABLE IS NOT ACCESSIBLE IN THE CHILD CLASS



# inheritance has various types:
# 1. single level inhertiance : when a single child inherit directly from the Parent
# 2. Multi level inheritance : when a child inherits from another child which itself inherits from the parent
# 3. Multiple Inheritance : When more than one parent classes exist in a child class.

# example
# Employee relates to Admin(single level inheritance)
# Employee relates to admin which further relates to Accountant (Multi level inheritance)


#MULTIPLE INHERITANCE

class lecturer:
    def __init__(self,salary):
        self.salary = salary
class student:
    def __init__(self,gpa):
        self.gpa = gpa
class TAs(lecturer,student):
    def init(self,salary,gpa,name):
        super().__init__(self,salary)
        student().__init__(self,gpa)
        
#Abstraction : showing only necessary stuff and hiding the Internaldetails

# abstract classes are a blueprint for other classes. We don't create any instance of these classes but create other classes based on these classes
# to create abstract classes we use python module named abc (abstraction based classes)

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass
    
class Lion(Animal):
    def makesound(self):
        print("Roar")
class COW:
    def makesound(self):
        print("moo")
lion = Lion()
lion.makesound()
cow = COW()
cow.makesound()

# polymorphism : many forms poly means many and morphism means forms
# multiple functions with same name
# 1. function overriding
# redefining a function in a child class which already exists in the parent class is called function overriding. EXAMPLE:

class Punjabi_Master:
    def designation(self):
        print("Designation is Punjabi Teacher")
class Angrezi_Master(Punjabi_Master):
    def designation(self):
        print("Designation is Angrezi Master")
ram = Angrezi_Master()
ram.designation() #angrezi master instead of punjabi master because of function overriding 

# 2. ducktyping
# if something walks like a duck and quakes like a duck we can treat it like a duck irrespective of classes
class Punjabi_Master:
    def designation(self):
        print("Designation is Punjabi Teacher")
class Angrezi_Master():
    def designation(self):
        print("Designation is Angrezi Master")
ram = Angrezi_Master()
ram.designation() 
# even if the above two classes aren't related we can name the function same as both functions in two classes do the same job which is printing the designation.
