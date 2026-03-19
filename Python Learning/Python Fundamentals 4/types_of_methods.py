class Laptop:
    storage_type = "SSD"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        
    @classmethod # it is a decorator used to create a class method (which can only access class attributes and no object attributes)
    def get_info(self):
        print(f"laptop has {self.storage_type} Storage")
        
    def get_info(self):
       print(f"laptop has {self.ram} RAM and {self.storage} {self.storage_type} Storage")
    
    @staticmethod # This decorator is used to create a static method. it is a stand alone function defined in a class (it doesn't take anything from the class or the constructor)
    def discount(price,percentage):
        print(f"price is {price} of percentage {percentage}")    
l1 = Laptop("16gb","256gb")
l2 = Laptop("8gb","512gb")

l1.get_info()
l1.discount(23,58)