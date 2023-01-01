from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Response
from .. hashing import Hash

from .. import schemas, database, models


router = APIRouter()


@router.post('/user', response_model=schemas.ShowUser, tags=['user'])
def create_user(request: schemas.User,  db: Session = Depends(database.get_db)):
    # hashedPassword = pwd_cxt.hash(request.password)

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


@router.get('/user', tags=['user'])
def get_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['user'])
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with {id} not found")

    return user
