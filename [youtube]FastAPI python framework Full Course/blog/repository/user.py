from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response
from .. import models
from .. import schemas
from .. hashing import Hash


def create(db: Session, request):
    new_user = models.User(
        firstname=request.firstname,
        lastname=request.lastname,
        email=request.email,
        password=Hash.bcryot(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def get_user_by_id(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with {id} not found")
    return user
