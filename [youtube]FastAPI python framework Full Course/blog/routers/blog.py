from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response

from .. import schemas, database, models

router = APIRouter(
    tags=['blogs'],
    prefix='/blog'
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.get('/', response_model=List[schemas.Blog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    return blog


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int,  db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()

    return {"details": f"blog with id {id} has been deleted"}


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    blog.update(request)
    db.commit()

    return blog
