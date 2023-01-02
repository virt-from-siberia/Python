from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Response
from . import schemas, models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

from .routers import blog, user, authentication


models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
