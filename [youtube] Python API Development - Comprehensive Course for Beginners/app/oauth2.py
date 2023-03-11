from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models

SECRET_KEY = '23098345987456'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60

o2auth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str, credentials_expiration):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_expiration

        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_expiration

    return token_data


def get_current_user(token: str = Depends(o2auth2_scheme),
                     db: Session = Depends(database.get_db)):
    credentials_expiration = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials', headers={
            'WWW-Authenticate': 'Bearer'
        })

    token = verify_token(token, credentials_expiration)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
