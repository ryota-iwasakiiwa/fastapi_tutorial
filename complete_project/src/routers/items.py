from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..crud import crud
from ..schemas import items as schemas_item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("/{user_id}", response_model=schemas_item.Item)
def create_item(
    user_id: int,
    item: schemas_item.ItemCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@router.get("/", response_model=list[schemas_item.Item])
def read_items(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limt=limit)
    return items