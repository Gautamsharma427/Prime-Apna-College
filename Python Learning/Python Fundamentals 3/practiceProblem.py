info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

subjects = set()
# print(info[0][1])
for tup in info:
    subjects.add(tup[1])
    
print("The Unique subjects in it are: ")
print(subjects)
for data in info:
    if(data[1]=="English"):
        print(data[0])
    else:
        continue
    
# 1. get students as elements and empty sets as their subjects
# 2. fill those sets with their respective subjects

students = {}

for student in info:
    if(student[0] in students):
        students[student[0]].add(student[1])
    else:
        
        students.update({student[0]:set()})
        students[student[0]].add(student[1])
print(students)