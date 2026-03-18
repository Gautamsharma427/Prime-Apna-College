info = {
    "name":"Shradha",
    "cgpa":9.6,
    "subjects":["maths","science"]#you can also embed other datatypes in a dictionary like list in this case   
}
print(info)#would print the dictionary
print(type(info))#would give the type dict which means dictionary

#just like we have index in lists and tuples we have keys in a dictionary through which we can access values
print(info["name"])#would give the value of name which is shradha

#dictionary is a mutable datatype and we can modify it like this:
info["name"]="Shraadha"
print(info["name"])#would give Shraadha instead of shradha as it is modified
print(info.get("name"))#would print the value of name which is Shraadha
#dictionary is a unoredered datatype

#METHODS OF DICTIONARY
print(info.keys())#would print all the keys. by default its type is dictionary_lkeys but we can type cast into lists
keys = list(info.keys())
print(keys,type(keys))#keys is a list which contains a list of all the dictionary keys

print(info.items())#would print all the items of the dictionary info
print(info.update({
    "city":"Delhi"
    }))#would add the keyvalue pair in the dictionary.
print(info)#would print the updated dictionary