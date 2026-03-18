#sets are a collection of unique elements. it contains only immutable datatypes and not mutable datatypes.
s1 = {1,2,2,2,2,2,2,3,4,5,6,7,7,7,7,8}
print(type(s1))
print(s1)#would remove the repeating elements and only print the elements once as set contains only unique elements.
print(len(s1))#would give 8
#python sets are mutable and unordered meaning they don't have a definite order and can be updated
s1.add(89)#would add 89 in a set s1
print(s1)

#creating a empty set
# we use set() function to create a set which is empty as blank curly braces would create a dictionary instead of a set
empty_set = set()
s1.pop()#would remove a random value
print(s1)
#we can also clear a set and make it empty by using a method:
s1.clear()#would delete all the elements of the set s1
#we can do union and intersection b/w two elements using the methods union and intersection
print(s1.union(empty_set))