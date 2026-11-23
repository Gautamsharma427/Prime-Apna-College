from fastapi import FastAPI,HTTPException
from main import PROD,getLowStockProducts,searchProduct,updateDB
from pydantic import BaseModel
from pathlib import Path
app = FastAPI()

class Product(BaseModel):
    name: str
    SKU: str
    Price: float
    Quantity: int
    ReorderLevel: int


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