from fastapi import FastAPI, Path, Query, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}/")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to update", ge=0, le=1000)],
    importance: Annotated[int, Body(gt=0)],
    # q: Annotated[str | None, Query()] = None,
    q: str | None = None,
    item: Annotated[Item | None, Body(embed=True)] = None,
    user: User | None = None,
):
    results = {"item_id": item_id, "importance": importance}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results

