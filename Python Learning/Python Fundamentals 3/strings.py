#A String is a sequence of charcters
name = "Apna College" # is a example of a string
teacher = "shradha Khapra"
# multiple operations can be performeds on strings
print(len(name))#prints the length of string
naming = name+" "+teacher
print(naming)#would become "Apna College shradha Khapra". This is conactination.

#strings support indexing: 
#name[0] = "A" & name[1]="p" and so on..

# string slicing
print(name[0:4])# would print "Apna" as it starts from 0 and ends at 3
print(name[5:])# would print "College" as it starts from 5 and goes till the end of the string
print(name[:6])# would print "Apna C" as it starts from the beginning and ends at 5
print(name[-7:])# would print "College" as it starts from the end and goes till the end of the string
print(name[::2])# would print "AaCleg" as it starts from the beginning and goes till the end of the string with a step of 2

#F Strings
age = 20
print(f"My age is {age}")# would print "My age is 20" as it uses f-string to format the string with the value of age variable

#normal string formatting
print("My age is {}".format(age))# would print "My age is 20" as it uses the format method to format the string with the value of age variable.

#index based string formatting
print("My age is {0}".format(age))# would print "My age is 20" as it uses the format method with index to format the string with the value of age variable.