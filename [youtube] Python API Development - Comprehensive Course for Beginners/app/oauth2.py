from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas

SECRET_KEY = '23098345987456'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

o2auth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str, credentials_expiration):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_expiration

        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_expiration

    return token_data


def get_current_user(token: str = Depends(o2auth2_scheme)):
    credentials_expiration = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials', headers={
            'WWW-Authenticate': 'Bearer'
        })

    return verify_token(token, credentials_expiration)
