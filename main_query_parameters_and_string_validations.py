from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[
        list[str] | None,
        Query(
            title="Query string test",
            description="Query string for the items to search in the database that have a good match",
            deprecated=True,
        )
    ] = ["foo", "bar"],
    a: Annotated[
        str | None,
        Query(alias="item-query",)
    ] = None,
    hidden_query: Annotated[
        str | None,
        Query(include_in_schema=False)
    ] = None,
):
# async def read_item(q: Annotated[str | None, Query(min_length=3)]):
# async def read_item(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    if a:
        results.update({"a": a})
    if hidden_query:
        results.update({"hidden_query": hidden_query})
    return results