from fastapi import FastAPI,HTTPException
from main import PROD,getLowStockProducts,searchProduct
from pydantic import BaseModel

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