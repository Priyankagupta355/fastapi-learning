from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# about route
@app.get("/about")
def about():
    return {"message":"this is about page"}

# users page
@app.get("/users")
def users():    
    return {
        "users":["Priyanka","chanchal","shivani","pari"]
    }