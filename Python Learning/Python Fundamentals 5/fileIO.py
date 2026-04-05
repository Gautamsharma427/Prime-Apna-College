import os
class file_io:
    # File io is a file input output opeartion in python.
    # file operations 
    def __init__(self,data):
        f = open("./sample.txt",'r+') # two main modes : R and W -> Read and Write
        print(f.read())
        print(f.write("The file operations are completed successfully."))
        f.close()
        # with keyword
        with open('sample.txt','r') as s:
            data = s.read()
            print(data, len(data))
            s.close()
            # self.deleting_files('sample.txt')
            
    @staticmethod
    def deleting_files(title):
        os.remove(title)
        print("FILE DELETED SUCCESSFULLY!")
    @staticmethod
    def word_search(word,file):
        with open(file,'r') as a:
            occurences = 0
            for line in a:
                if(line.find(word)!=-1):
                    occurences+=1
                else:
                    pass
            print(f"I found {occurences} occurences of {word} in {file}")
            a.close() 

FILE = file_io("sample.txt")
FILE.word_search(file="data.txt", word="Python")
    