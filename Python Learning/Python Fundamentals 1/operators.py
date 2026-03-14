'''
Operators are of multiple types:
assignment operator
logical operator
Arithmetic operator
relational/comparision operator

operands are on which operation is performed
operator is which tells what operation to perform

'''

#arithmetic operators
a = 10
b = 5

SUM = a+b
DIV = a/b
MULTIPLICATION = a*b
SUBSTRACTION = a-b
MODULO = a%b #WOULD PRINT REMAINDER AFTER DIVISION(0 IN THIS CASE)
ASTERISK = a**b #would print a to the power of b

#relational operators : return true or false based on condition provided
a_less_than_b=a<b#false
a_greater_than_b=a>b#true
a_equal_to_b = a==b#false
a_not_equal_to_b = a!=b#true

#assignment operators
a = b #value of b is being assigned to a
a +=b #add b to a 
a *=b #multiply b to a
a /=b #divide b to a 

#Logical Operators
#1. Not (!) prints the opposite value (true if false, false if true)
#2. Or (||) prints true even if one value is true 
#3. and(&&) prints true only if both values or conditions are true
print(not a_equal_to_b)#true(opposite of false)


#operator precedence
# It is the priority order of execution of operators
#(), **, */%, +-, relational, logical
