#1
string = "madam"
string_reversed = ""

for letter in string:
    string_reversed= letter+string_reversed
if(string_reversed==string):
    print("string is a palindrome")
else:
    print("string is not a palindrome")
    
#2
l = [5,10]
SUM = 0
length = len(l)
for item in l:
    SUM = SUM+item
print(f"average is {SUM/length}")

#3
list1 = [1,2,7]
list2 = [2,4,5]

for element in list2:
    list1.append(element)
list1.sort()
print(list1)

#4
tup1 = (0,1,2,3,4,5,6,7,8,9,10,11,12)

even_tup = []
odd_tup = []

for integer in tup1:
    if(integer%2 == 0):
        even_tup.append(integer)
    elif(integer%2!=0):
        odd_tup.append(integer)
       
even_tup = tuple(even_tup)
odd_tup = tuple(odd_tup)
print(even_tup,type(even_tup))
print(odd_tup,type(odd_tup))

#5
dictionary = {
    "Ram":43,
    "shyam":97,
    "lakshman":89,
    "pramodh":56,
    "Dheeru":62
} 
option = input("Enter the Key for the task you want to perform: ")
if option == "A":
    name = input("Enter the name of the Student: ")
    mark = int(input("Enter the Marks of the Student: "))
    dictionary.update({name:mark})
    print("updated successfully")
elif option == "B":
    name = input("Enter the name of the student whose marks you want to update: ")
    marks = input("How many marks: ")
    keys = list(dictionary.keys())
    if name in keys:
        dictionary[name] = marks
        print("Updated successfully")
    else:
        print("Sorry No Student with this name...")
elif option == "C":
    name = input("Whose marks you want to see?: ")
    print(dictionary[name])
elif option == "D":
    print(dictionary)
    
#6
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dictionary = {}
for fruit in words:
    length = len(fruit)
    dictionary.update({fruit:length})
print(dictionary)

#7
stringg = "I am a fighter "
spaces = 0
for word in stringg:
    if word == " ":
        spaces+=1
    else:
        continue
print(f"Number of spaces in string were {spaces}")

#8
# share common elements
list1 = [1, 2, 3]
list2 = [3, 4]
# share no common elements
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
set1 = set()
set2 = set()
for element in list1:
    set1.add(element)
for element in list2:
    set2.add(element)
if(set1.isdisjoint(set2)):
    print("Share no common elements")
else:
    print("share common elements")

#9
repeating = [1,2,2,2,2,3,4,3,4,4,3,3,5,6,7,8,5,7,8,9,10,11,12,13]
repeat = set()
duplicates = set()
for element in repeating:
    if element in repeat:
        duplicates.add(element)
    else:
        repeat.add(element)
    
print(duplicates)

#10
string = "Pseudopodia"
unique = set()
for letter in string:
    unique.add(letter)
print(unique,len(unique))