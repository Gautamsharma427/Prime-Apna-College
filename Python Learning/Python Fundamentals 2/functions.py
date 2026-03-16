# Functions are blocks of code which do a specific task. They are reusable and callable when required.
# Definition of function is where the logic of the function is written
# Calling a funcition means reusing a function in a program
# Syntax of function definition
# def function_name(parameters):
#     logic of the function
#     return value
def hello():
    print("Hello")
# above is example of definition of a function
hello()
# above is the example of calling a function
# function takes a input do some processing and returns a output. 
# parameters are values of function which we pass into them
def sum(a,b):
    s = a+b
    return s

# s is the return value
# a and b are paramerters of sum function which we pass like this:

sum(3,5)#would return 8

# defining a function which returns the average of three numbers a b and c
def avg(a,b,c):
    return (a+b+c)/3
print(avg(2,2,2))
#passing a default value in a function
def sum(a,b=1):
    return (a+b)
# so b will be 1 by default and only change when its value is passed a function call
print(sum(3))#would give 4 by default cuzz value of 1 is passed by default to b
print(sum(3,2))#would give 5 cuzz value of 2 is given in function which will be added to 3.
#Types of Function
# 1. Built in Functions
# - print()
# - range()
# - type()
# 2. User Defined Functions
# - The functions defined by user are called user defined functions. Examples include all the functions which we defined above

# LAMBDA FUNCTIONS : These are the functions which calculate the value of a expression given in the function and calculate the answer on basis on the sum varaible
# Below is the syntax of a Lambda function definition
sum_of_abc = lambda a,b,c:a+b+c
print(sum_of_abc(3,4,5))

# factorial of any number n (n!)
def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    return factorial
print(factorial(3))