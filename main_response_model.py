from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get("/items/", response_model=list[Item])
async def get_items() -> Any:
    return [
        {"name": "Foo", "price": 42.0},
        {"name": "Bar", "price": 42.0},
        # Item(name="Portal Gun", price=42.0),
        # Item(name="Plumbus", price=32.0),
    ]

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

@app.get("/portal/", response_model_exclude_unset=True)
async def get_portal(item_id: str) -> Item:
    return items[item_id]

# @app.get("/portal/", response_model=None)
# async def get_portal(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app.get("/teleport/")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
