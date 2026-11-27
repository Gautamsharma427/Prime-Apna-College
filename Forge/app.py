from fastapi import FastAPI,HTTPException
from main import PROD,getLowStockProducts,searchProduct,updateDB
from pydantic import BaseModel, Field,ConfigDict
from pathlib import Path
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