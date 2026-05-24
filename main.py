from fastapi import FastAPI
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