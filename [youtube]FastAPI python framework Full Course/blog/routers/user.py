from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response

from .. hashing import Hash
from .. import schemas, database, models
from .. repository import user


router = APIRouter(tags=['user'], prefix='/user')


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,  db: Session = Depends(database.get_db)):
    return user.create(db, request)


@router.get('/')
def get_all_users(db: Session = Depends(database.get_db)):
    return user.get_all(db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user_by_id(db, id)
