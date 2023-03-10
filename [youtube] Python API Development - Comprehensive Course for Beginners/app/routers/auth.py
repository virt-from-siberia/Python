from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authenticated'])


@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.Token)
def login_user(user_credentials: OAuth2PasswordRequestForm = Depends(),
               db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')

    # create token
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    # return token
    return {'access_token': access_token, 'token_type': "bearer"}
