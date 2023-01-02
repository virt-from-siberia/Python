from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response
from .. import models
from .. import schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, request):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"details": f"blog with id {id} has been deleted"}


def get_by_id(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")
    return blog


def update(db: Session,  id: int, request):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    blog.update(request)
    db.commit()
    return blog
