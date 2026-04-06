# learning about the JSON Module in Python
# JSON stands for JavaScript Object Notation
import json # used to import the json module in python
# json format is very simlar to python dictionaries 
data = '{"name":"John Doe","age":32,"job":"engineer","isTeacher":false}'
print(data)
print(type(data)) # its a python string not a JSON file/data

# json.loads() function is used to convert JSON string into a python dictionary/object
# json.dumps() function is used to convert a python dictionary/object into a JSON string

# we can use json module to convert data into a python object from a javascript json format
data_python = json.loads(data) #.loads() function converting json string to python dictionary
print(data_python)
print(type(data_python)) # its a python dictionary not a string

#we can also convert Python dictionary to JSON String
python_obj = {
    'name' : 'Tony Stark',
    'money_status': 'Billioniare',        
    'Job'  : 'Iron Man'
} # this is a python dictionary

json_string = json.dumps(python_obj)

print(python_obj,type(python_obj))
print(json_string,type(json_string))

# the S in the dumps and loads stands for string so it means load string and dump string which refers to the json strings


# these two functions will be used when we are dealing with strings and dictionaries. but in majority cases we will be dealing with JSON files so let's learn how to deal with them
with open(".\data.json",'r') as file:
    data = json.load(file) #.load() function converts a json data into a python dictionary from a file
    print(data,type(data))
    file.close()
with open(".\data.json","w") as file:
    json.dump(python_obj,file,indent=4,sort_keys=True) # converts a pythoin object into a json format and then pushes into the file and gives indentation of four spaces and sorts keys in ascending order
    file.close()