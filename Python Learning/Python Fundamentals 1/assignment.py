#1. 
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
print(f"Hello {name}, you are {age} years old!")

#2. 
a = int(input("Enter a Number"))
b = int(input("Enter another number"))
print(f"sum {a+b}, product {a*b}, difference {a-b}, quotient {a/b}")

#3
a = int(input("Enter a Number"))
b = int(input("Enter another number"))
c = float(input("Enter a Float"))
print(f"average of the three numbers is {(a+b+c)/3}")

#4
num = "45"
num = int(num)
print(num,type(num))
num = float(num)
print(num,type(num))
num = str(num)
print(num,type(num))

#5
x = 10+3*2**2 # 10+3*4 = 10+12 = 22
print(x)

#6
c = int(input("Enter a number: "))

d = int(input("Enter another number: "))
e = c
c = d
d = e
print(f"After swapping: c = {c}, d = {d}")

#7
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

#8
r = float(input("enter the radius: "))
PI = 3.14
print("Answer is: ",PI*r**2)

#9
P = float(input("Enter the principle Amount: "))
R = float(input("Enter the rate: "))
T = float(input("Enter the Time Period: "))
SI = (P*R*T)/100
print(SI)

#10
Num1 = float(input("Enter a Floating Number: "))
#43.32
Num2 = float(int(Num1))
num3 = Num1 - Num2
print(f"Integer Part: {Num2} Fractional Part: {num3}")