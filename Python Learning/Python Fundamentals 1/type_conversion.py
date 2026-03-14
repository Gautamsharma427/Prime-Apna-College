#Conversion is of two types :
#typeconversion: conversion performed automatically by python. it is implicit
#typecasting: conversion done manually by the programmer in the program is called typecasting. it is explicit. it is only possible with compatible datatypes.

ans = int(1+0.5)
ans2 = 1+0.5
print(ans,type(ans))
print(ans2,type(ans2))

ans = int("3342")
print(ans,type(ans))

ans = bool(ans)
print(ans,type(ans))# non zero values are true and zero is false
