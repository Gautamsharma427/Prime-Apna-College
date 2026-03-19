class Product:
    count = 0
    
    def __init__(self,name,price):
        self.name = name
        self.price = price  
        Product.count+=1
    def get_info(self):
        print("The Product is {self.name} and it costs {self.price} Rupees")
    
    @classmethod
    def get_count(cls):
        print(f"Count is {cls.count}")
    @staticmethod
    def discount(price,percentage):
        print(f"Final Price is {price - (percentage/100)*price}")
    
    
product1 = Product("Laptop",32_000)
product2 = Product("Phone",10_000)
product3 = Product("Pen",10)

Product.get_count()
Product.discount(10,1)