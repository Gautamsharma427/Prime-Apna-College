#for loops are used to iterate over a sequence (string in this example)
string = "hello"
#count starts from h and goes till o
for count in string:
    print(count)
#range function is used to generate a sequence of numbers
for i in range(0,10):
    print(i)
#range(start, stop, step)
for i in range(0,10,2):
    print(i)

#program to print the sum of n natural numbers.
n = int(input("Enter the number."))
sum = 0
for i in range(1,n+1):
    sum = sum+i

print(sum)
