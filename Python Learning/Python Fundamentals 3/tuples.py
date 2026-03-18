#Tubles are also a datatype of python the difference is that they are immutable
tup = (1,2,3,4,5)
print(type(tup))

# Tuples are similar to lists and the only difference is that we can't assign value as they are immutable. also the methods for tuples are also different and the list methods don't work on tuples

# we can't create a single value of tuple in python without a comma
single_value_tuple = (1) #would become a integer instead of a tuple so its not declared this way❎
single_value_tuple = (1,)#comma tells python that this is a tuple

# also we can similarly iterate over a tuple just like list 
for value in tup:
    print(value)

# Tuple methods
print(tup.index(2)) # would return 1 as the index of 2 in tuple tup is 1
print(tup.count(2)) # would return how many times a value(2 in this case) is occuring in a tuple
