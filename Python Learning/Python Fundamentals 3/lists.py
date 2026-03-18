#lists are a type of a mutable datatype in python which is used to store a sequence of values

#following is the syntax of a list
names = ["Ram","Shyam","Gopal","Shradha"]
marks = [32,49,39,23]
# index can also be used in a list
print(len(names))
print(len(marks))
print(marks[1])
marks[1] = 343 # this is possible is lists but not in strings because lists are mutable unlike strings which are immutable
#lists can be sliced similarly to strings
print(marks[1:])
print(marks[:])
#Note:other functions of slicing are also similar
#Methods of a List
marks.append(100)
print(marks)#100 will be appended to the last of the list
marks.insert(1,10)#index,value
print(marks)#10 will be inserted at index 1 and others would be pushed forward or backwards
marks.reverse()# is used to reverse a list

#Loops on lists(iterating a list with a for loop)
for value in marks:
    print(value)

#finding a x in a list
# The way of searching which we used is called linear search.
# let's say we have a list which contains some x and we need to find it 
numbers = [2,4,60,23,54,32,20]
x = 54
idx = 0
for num in numbers:
    if(num==x):
        print(f"{x} is found at {idx}")
    idx+=1