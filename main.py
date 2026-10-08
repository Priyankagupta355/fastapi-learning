from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# About Route
@app.get("/about")
def about():
    return {"message": "This is about page"}


# Users Route
@app.get("/GETusers")
def users():
    return {
        "users": ["Priyanka", "Chanchal", "Shivani", "Pari"]
    }


# Path Parameter
@app.get("/usersID/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }

# Query Parameter
@app.get("/Users")
def get_user(name:str = None):
    return {"Name":name}

@app.get("/products")
def get_user(limit: int = 10):
    return {"limit": limit}

@app.get("items")
def get_users(name: str = None, price: int=0):
    return {
        "name":name,
        "price":price
    }

#Request body & POST request
@app.post("/create-user")
def create_user(user: dict):
    return {
        "message": "User Created",
        "data": user
    }