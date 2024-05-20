from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

app = FastAPI()

# async def get_db():
#     db = DBSession()
#     try:
#         yield db
#     finally:
#         db.close()

# async def dependency_a():
#     dep_a = generate_dep_a()
#     try:
#         yield dep_a
#     finally:
#         print("Cleaning up dep_a")

# async def dependency_b(dep_a=Annotated[DepA, Depends(dependency_a)]):
#     dep_b = generate_dep_b()
#     try:
#         yield dep_b
#     finally:
#         print("Cleaning up dep_b")

# async def dependency_c(dep_a=Annotated[DepB, Depends(dependency_b)]):
#     dep_c = generate_dep_c()
#     try:
#         yield dep_c
#     finally:
#         print("Cleaning up dep_c")


data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}

class OwnerError(Exception):
    pass

class InternalError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except Exception as e:
        print("Oops, we didn't raise again, Britney 😱")
        raise
    # except OwnerError as e:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Owner error: {e}")

@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    item = data[item_id]
    # if item["owner"] != username:
    #     raise OwnerError(username)

    if item_id == "portal-gun":
        raise InternalError(f"The portal gun is too dangerous to be owned by {username}")
    if item_id != "plumbus":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found, there's only a plumbus here")
    
    return item