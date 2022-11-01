from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from db import db_user

from db.database import get_db
from fastapi import HTTPException, status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = 'dd9bc00c8ec325ddcb50d3516564b23d44ad47a79ca828733178c17d816d48e5'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail='Could not validate credentials', headers={
            'WWW-Authenticate': 'Bearer'})

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db_user.get_user_by_username(db, username)
    if user is None:
        raise credentials_exception

    return user
