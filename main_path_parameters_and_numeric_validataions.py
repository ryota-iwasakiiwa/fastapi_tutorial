from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[
        int,
        Path(title="The ID of the item to get", gt=0, le=1000)
    ],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
