#1
with open('log.txt','w') as file:
    a = [input("Enter a Name: ") for i in range(5)]
    print(a)
    for i in a:
        file.writelines(i+'\n')
with open('log.txt','r') as file:
    print(file.read())

#2
with open('log.txt','a') as file:
    file.write("program ran successfully")
    
#3
num_list = [5,10,15,20,25]
greater_list = [i for i in num_list if i>15]
print(greater_list)

#4
import json
with open('cities.json','r') as cities:
    document = json.load(cities)
    print(document)
    print(type(document))
    
with open('cities.json','w') as cities:
    new_city = input("ENTER A CITY NAME: ")
    new_popu = input("ENTER ITS POPULATION: ")
    document.update({
        f"{new_city}": f"{new_popu}"
    })
    json.dump(document,cities,indent=4)

#5
try:
    with open("data2.txt",'r') as file:
        print(file.read())
except Exception as e:
    print("FIle Not Found")