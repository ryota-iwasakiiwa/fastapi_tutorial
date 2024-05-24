from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_active_user
from ..crud import crud
from ..schemas import items as schemas_item
from ..schemas import users as schemas_user

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("/", response_model=schemas_item.Item)
def create_item(
    item: schemas_item.ItemCreate,
    current_user: Annotated[schemas_user, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=current_user.id)

@router.get("/", response_model=list[schemas_item.Item])
def read_items(
    skip: int=0,
    limit: int=100,
    db: Session = Depends(get_db)
):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items