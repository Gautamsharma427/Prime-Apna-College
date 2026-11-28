from fastapi import FastAPI,HTTPException
from main import PROD,getLowStockProducts,searchProduct,updateDB,getMovements,saveMovements,addSupplier,getSuppliers,removeSupplier
from pydantic import BaseModel, Field,ConfigDict,EmailStr
from datetime import datetime
from typing import Literal
app = FastAPI()

class Product(BaseModel):
    model_config = ConfigDict(str_strip_whitespace = True)
    name: str = Field(min_length = 1)
    SKU: str = Field(min_length=1,max_length = 5)
    Price: float = Field(ge=0)
    Quantity: int = Field(ge=0)
    ReorderLevel: int = Field(ge=0)

class UpdateProd(BaseModel):
    model_config = ConfigDict(str_strip_whitespace = True)
    name: str | None = None
    Price: float | None = None
    Quantity: int | None = None
    ReorderLevel: int | None = None

class NewProd(Product):
     pass

class StockIn(BaseModel):
    quantity: int = Field(gt=0)

class StockOut(StockIn):
    pass

class Movement(BaseModel):
    SKU : str
    type: Literal["stock-in", "stock-out"]
    quantity : int = Field(gt=0)
    previous_quantity:int = Field(ge=0)
    new_quantity:int = Field(ge=0)
    timestamp : str


class Supplier(BaseModel):
    ID : str
    name : str
    phone : str
    email : EmailStr
@app.get("/products")
def products():
    return PROD()

@app.get("/products/low-stock")
def lowStock():
    return getLowStockProducts(PROD())

@app.get("/products/{sku}")
def getProduct(sku:str):
    if(searchProduct(sku,PROD())==None):
        raise HTTPException(status_code=404, detail="product not found")
    else:
        return searchProduct(sku,PROD())
@app.post("/products")
def createProduct(product:Product):
    product = product.model_dump()
    products = PROD()
    for prod in products:
        if(prod['SKU']==product['SKU']):
            raise HTTPException(409,detail="product already exists")
    
    products.append(product)
    updateDB(products)
    return product

@app.patch("/products/{sku}",status_code=200)
def updateProduct(sku:str,prod:UpdateProd):
    prod = prod.model_dump(exclude_unset=True)
    products = PROD()
    found = False
    if not prod:
        raise HTTPException(400,detail="Details not provided")
    for product in products:
        if(product['SKU']==sku):
            found = True
            product.update(prod)
            break
    if not found:
        raise HTTPException(404,detail="Product Not Found")
    updateDB(products)
    return product

@app.put("/products/{sku}",status_code=200)
def replaceProduct(sku:str,newData:NewProd):
    newData = newData.model_dump(exclude = {"SKU"})
    newData["SKU"] = sku
    products = PROD()
    found = False
    for product in products:
        if product["SKU"] == sku:
            found = True
            product.update(newData)
            break
    if not found:
            raise HTTPException(404,detail="Product Not Found")
    updateDB(products)
    return product

@app.delete('/products/{sku}',status_code=204)
def deleteProduct(sku:str):
    products = PROD()
    found = False
    for product in products:
        if(product["SKU"]==sku):
            found = True
            products.remove(product)
            break
    if not found:
        raise HTTPException(404,detail="Product Not Found")
    updateDB(products)
    # no content on deletion request
@app.post("/products/{sku}/stock-in")
def stockIn(sku:str,value: StockIn):
    value = value.model_dump()
    products = PROD()
    found = False
    for product in products:
        if product["SKU"] == sku:
            prev_qty = product["Quantity"]
            found = True
            product["Quantity"] = product['Quantity']+value['quantity']
            break
    if not found:
        raise HTTPException(404,detail="Product Not found")
    updateDB(products)
    movement = Movement(SKU=sku,type="stock-in",quantity=value['quantity'],previous_quantity=prev_qty,new_quantity=product["Quantity"],timestamp=datetime.now().isoformat())
    saveMovements(movement.model_dump())
    response = {"SKU":sku,"previous_quantity":prev_qty,"added_quantity":value['quantity'],"new_quantity":product["Quantity"]}
    return response 

@app.post("/products/{sku}/stock-out")
def stockOut(sku:str,value: StockOut):
    value = value.model_dump()
    products = PROD()
    found = False
    if(value["quantity"]<0):
            raise HTTPException(422,detail="Detail Unprocessed! Entered Quantity is negative")   
    for product in products:
        if product["SKU"] == sku:
            if(value["quantity"]>product["Quantity"]):
                raise HTTPException(422,detail="Detail Unprocessed! Entered Quantity is more than the Present Quantity")
            prev_qty = product["Quantity"]
            found = True
            product["Quantity"] = product['Quantity']-value['quantity']
            break
    if not found:
        raise HTTPException(404,detail="Product Not found")
    
    updateDB(products)
    movement = Movement(SKU=sku,type="stock-out",quantity=value['quantity'],previous_quantity=prev_qty,new_quantity=product["Quantity"],timestamp=datetime.now().isoformat())
    saveMovements(movement.model_dump())
    response = {"SKU":sku,"previous_quantity":prev_qty,"quantity_out":value['quantity'],"new_quantity":product["Quantity"]}
    return response

@app.get("/product-history",status_code=200)
def prodHistory():
    return getMovements()

@app.get("/suppliers",status_code=200)
def sendSuppliers():
    return getSuppliers()
@app.post("/add-supplier",status_code=200)
def addSuppl(data:Supplier):
    suppliers = getSuppliers()
    data = data.model_dump()
    for supplier in suppliers:
        if supplier["ID"]==data["ID"]:
            raise HTTPException(detail="Supplier Already Exists! Data Unprocessed",status_code=422)
    addSupplier(data)
    return data

@app.delete("/suppliers/{id}",status_code=204)
def delSupplier(id:str):
    try:
        removeSupplier(id)
    except Exception:
        raise HTTPException(status_code=404,detail="Supplier Not Found")