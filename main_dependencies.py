from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

async def common_parameters(
    q: str | None = None,
    skip: int = 0,
    limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}

CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_item(commons: CommonsDep):
    return commons

@app.get("/users/")
async def read_user(commons: CommonsDep):
    return commons
