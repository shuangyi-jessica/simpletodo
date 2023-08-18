print("Hello, World!")

from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI() # create a fastAPI instance
MYTODOLIST = []
USERS = []

@app.get("/")
def read_root():
    return {"Hello": "World2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    item.price = 0
    return item

class ToDo(BaseModel):
    name: str
    description: str | None = None
    assignto: str | None = None

@app.get("/todos/")
def get_todoList():
    return MYTODOLIST

@app.post("/todos/")
def add_new_todo(todo:ToDo):
    if todo.assignto:
        if verify_user_exists(todo.assignto):
            MYTODOLIST.append(todo)
        else:
            raise HTTPException(status_code=400,detail="user not found",headers={"X-Error": "There goes my error"}, )
    else:
        MYTODOLIST.append(todo)
    return todo

class User(BaseModel):
    name: str
    username: str
    password: str

@app.get("/usernames/")
def list_usernames():
    usernamelist = []
    for username in USERS:
        usernamelist.append(username.name)
    return usernamelist

@app.post("/usernames/")
def add_user(user:User):
    USERS.append(user)
    return user.name

def verify_user_exists(name):
    for user in USERS:
        if user.username == name:
            return True
    return False

