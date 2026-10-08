from fastapi import FastAPI

app = FastAPI()


# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# About Route
@app.get("/about")
def about():
    return {"message": "This is about page"}


# Users Route
@app.get("/users")
def users():
    return {
        "users": ["Priyanka", "Chanchal", "Shivani", "Pari"]
    }


# Path Parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }