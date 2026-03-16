#1. 
salary = int(input("Enter your salary."))
if(salary<30000):
    print("tax rate is 5%")
elif (30000<salary<70000):
    print("tax rate is 15%")
else:
    print("Tax rate is 25%")

#2
def even_numbers(a,b):
    for i in range(a,b+1):
        if(i%2 == 0):
            print(i)
        else:
            continue
even_numbers(1,10)

#3,4,5
# input 123 output 1 2 3
def digit_print(num):
    num = str(num)
    num.replace(' ','')
    count = 0
    digit_count = 0
    for i in num:
        print(i,end=" ")
        count+=1
        digit_count = digit_count+int(i)
    print(count,end="\n")
    print(digit_count,end="\n")

#6
digit_print(123345)
def numbers_div_by_5_3():
    for i in range(1,101):
        if(i%5==0 and i%3==0):
            print(i)
        else:
            continue
print("\n")
numbers_div_by_5_3()

#7
def positive_or_negative():
    condition = True
    while condition:
        i = input("Enter a number or write quit to exit: ")
        if(i.lower()=="quit"):
            condition = False
            continue
        else:
            try:
                i = int(i)
                if(i<0):
                    print(f"{i} is Negative")
                elif(i>0):
                    print(f"{i} is positive")
                else:
                    print(f"{i} is zero")
            except Exception as e:
                print("Error occured! Plz Check your input")
positive_or_negative()

#8
def calculator(a,b,operation):
    if(operation=="+"):
        return a+b
    elif(operation=="-"):
        return a-b
    elif(operation=="*"):
        return a*b
    elif(operation=="/"):
        return a/b
print(calculator(1,2,"+"))
print(calculator(1,2,"-"))
print(calculator(1,2,"*"))
print(calculator(1,2,"/"))

#9
def is_prime(a):
    condition = True
    for i in range(2,a):
        if(a%i==0):
            condition=False
            print(f"{a} isn't a prime number it comes at {i}X{int(a/i)}={a}")
            break
        else:
            continue
    if(condition==True):
        print("Prime Number")
is_prime(35)

#10
def number_guessing_game():
    
    number = 35
    while True:
        guess = int(input("Enter your guess: "))
        if(guess<number):
            print("Too Low")
        elif(guess == number):
            print("You Won. Thanks for playing...")
            break
        else:
            print("Too High")
        
number_guessing_game()