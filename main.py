from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user = []


class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(new_user: User):
    user.append(new_user)
    return {
        "message": "User Created",
        "data": new_user
    }    

@app.put("/users/{user_id}")
def updated_user(user_id: int, user: User, notify: bool = False):
    if user_id < len(user):
        user[user_id] = user

        return {
            "message": "UserCreated",
            "notify": notify,
            "data": user
        }
    return {
        "error": "User not found"
    }