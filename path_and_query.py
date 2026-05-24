from mockdata import products
from fastapi import FastAPI,Request
app=FastAPI()
from mockdata import products
@app.get("/home")
def home():
  return "welcome to fast api "
@app.get("/contact")
def contact():
  return "contact us at 999999999"
@app.get("/products")
def get_products():
  return products
@app.get("/products/{product_id}")# path params
def get_one_product_id(product_id:int):
  for oneproduct in products:
    if oneproduct.get("id")==product_id:
      return oneproduct
  
    
  return {
  "error":"product id is not found" }
## query params 
@app.get("/greet")
def greet_user(name:str,age:int):
  return {
    "greet":f"hello{name}, how are your {age} "
  }
## if i have to insert n dynamic value of query params 
@app.get("/greets")
def greets_user(request:Request):
  print(request.query_params)
  return 

