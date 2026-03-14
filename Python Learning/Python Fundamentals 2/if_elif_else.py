# They are the statements which execute when a specific condition is true.
# In python there are three types of conditional statements:
# if (condition){ -> Checks the condition and if it is true it executes
# // code goes in here   
# }
# elif(condition){ -> always executes after if and executes if true
    # //code goes here
#}
#else{code goes here} -> always executes when no condition is true
age = 21
if(age<=18):
    print("you can't Drive")
    print("you can't vote")
elif(age>=120):
    print("you put the wrong age")
else:
    print("You can Drive")
    print("You can Vote")

#Traffic Lights Program
current_light = input("What is the light colour: ")
if(current_light=="red"):
    print("You can't go yet please wait")
elif(current_light == "yellow"):
    print("You will be able to go shortly...")
elif(current_light == "green"):
    print("You can Go now")
else:
    print("There is no such colour please try again..")
    
#Checking if child or not
age = int(input("Age: "))
if(age<13):
    print("Child")
elif(13<=age<18):
    print("teenager")
else:
    print("adult")

#Password and Username Program
USER = input("Username: ")
PASSWORD = input("Password: ")

if(USER=="admin" and PASSWORD=="pass"):
    print("Logged In Successfully")
elif(USER!="admin" and PASSWORD!="pass"):
    print("Both Password and Username are incorrect")
elif(USER!="admin"):
    print("Username is incorrect!")
elif(PASSWORD!="pass"):
    print("Password is incorrect!")

# Odd or Even Number detector
num = int(input("NUMBER: "))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")
    
#NESTING IS WHEN YOU USE IF ELSE IN ANOTHER IF ELSE Statement.