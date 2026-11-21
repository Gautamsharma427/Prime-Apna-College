import json
from pathlib import Path
import sys
def getLowStockProducts(products):
    lowStock = []
    for product in products:
        if product["Quantity"] <= product["ReorderLevel"]:
            lowStock.append(product)
    return lowStock
def addProduct(products):
    name = input("Product-name: ")
    SKU = input("SKU: ")
    Price = float(input("Price: "))
    Quantity = int(input("Quantity: "))
    ReorderLevel = int(input("Reorder level: "))
    for product in products:
        if(product["SKU"]==SKU):
            print("SKU already found!")
            return
        else:
            continue
    return {"name":name,"SKU":SKU,"Price":Price,"Quantity":Quantity,"ReorderLevel":ReorderLevel}
def searchProduct(sku,products):
    found = False
    for product in products:
        if product["SKU"] == sku:
            print(product)
            found = True
    if not found:
        print("Product wasn't found!")

def updateProduct(sku,new_stock,products):
    try:
        for product in products:
            if product["SKU"] == sku:
                product["Quantity"] = new_stock
                break
    except Exception as e:
        print("updation failed plz check!")

if __name__ == "__main__":
    try:
        file_path = Path(__file__).resolve().parent / "products.json"
        f = open(file_path,"r")
        products = json.load(f)
        f.close()
    except Exception as e:
        print("Couldn't Open! Database corrupt or not exist! Plz check!")
        sys.exit()
    print("==============================")
    print("FORGE INVENTORY")
    print("==============================")
    while True:
        print("1. Add Product\n2. View All Products\n3. Search Products\n4. Update Stock\n5. Low Stock Report\nPress -1 to exit")
        try:
            option = int(input("Choose an option: "))
        except Exception as e:
            print("Please choose a valid option!\n")
            continue
        if option == 1:
            products.append(addProduct(products))
            with open(file_path,"w") as f:
                json.dump(products,f,indent=4)
        elif option == 2:
            print(products)
        elif option == -1:
            print("Thank You for using the app! Exiting...")
            break
        elif option == 3:
            sku = input("Enter the sku of product you're searching: ")
            searchProduct(sku,products)
        elif option == 4:
            sku = input("Enter sku of the product you want to update the stock of: ")
            new_stock = int(input("The New Stock Amount: "))
            updateProduct(sku,new_stock,products)
            with open(file_path,"w") as f:
                json.dump(products,f,indent=4)

        elif option == 5:
            print(getLowStockProducts(products))
    with open(file_path,"w") as f:
        json.dump(products,f,indent=4)