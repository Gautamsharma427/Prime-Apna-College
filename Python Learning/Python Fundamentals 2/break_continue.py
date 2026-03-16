#break keyword is used to terminate a loop prematurely when a certain condition is met.
#continue keyword is used to skip the current iteration of a loop and move on to the next 
# =========================================================================================
#printing odd numbers between 0 to 10 using continue statement
i = 0
while(i<10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
    
for n in range(1,i+1):
    if(n%2 == 0):
        break
    print(n)
     