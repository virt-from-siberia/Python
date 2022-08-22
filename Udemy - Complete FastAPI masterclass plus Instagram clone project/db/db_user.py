from sqlalchemy.orm.session import Session

from db.hash import Hash
from schemas import UserBase
from db.models import DbUser


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    # Handle any exeptions
    return db.query(DbUser).filter(DbUser.id == id).first()


def update_user(db: Session, id: int, request: UserBase):
    # Handle any exeptions
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


def delete_user(id: int, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    # Handle any exeptions
    db.delete(user)
    db.commit()
    return 'ok'
