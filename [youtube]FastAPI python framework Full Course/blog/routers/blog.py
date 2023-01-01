from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response

from .. import schemas, database, models
from .. repository import blog

router = APIRouter(
    tags=['blogs'],
    prefix='/blog'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(db, request)


@router.get('/', response_model=List[schemas.Blog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.get_by_id(db, id)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int,  db: Session = Depends(database.get_db)):
    return blog.delete(db, id)


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(db, id, request)
