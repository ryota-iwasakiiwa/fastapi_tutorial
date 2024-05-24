from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_active_user
from ..crud import crud
from ..schemas import users as schemas_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", response_model=schemas_user.User)
def create_user(
    user: schemas_user.UserCreate,
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas_user.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

@router.get("/mypage", response_model=schemas_user.User)
def read_user(
    current_user: Annotated[schemas_user, Depends(get_current_active_user)],
):
    return current_user