from fastapi import FastAPI

from .routers import items, users
from . import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)