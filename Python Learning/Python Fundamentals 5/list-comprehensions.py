square_list = [x*x for x in range(0,9)] # This is a list comprehension that contains the squares of numbers from 0,9 with 9 excluded

print(square_list)

odd_square_List = [i*i for i in range(0,9) if (i%2!=0)]
print(odd_square_List)

numbers = [-1,9,3,-2,-3,-34]
positve_numbers = [0 if num<0 else num for num in numbers]
print(positve_numbers)

words = ["hello","world","programming","python","makemoney"]
WORDS = [i.upper() for i in words]
print(WORDS)
