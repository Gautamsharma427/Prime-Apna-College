class file_io:
    # File io is a file input output opeartion in python.
    # file operations 
    def __init__(self,data):
        f = open("./sample.txt",'r+') # two main modes : R and W -> Read and Write
        print(f.read())
        print(f.write("The file operations are completed successfully."))
        f.close()

FILE = file_io("sample.txt")
