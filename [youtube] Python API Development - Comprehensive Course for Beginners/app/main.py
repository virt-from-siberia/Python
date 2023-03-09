from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session

from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='pythonApiDevelopment',
            user='postgres', password='postgres',
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to PostgreSQL was successful")
        break
    except Exception as error:
        print('Could not connect to PostgreSQL')
        print("error: ", error)
        time.sleep(2)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
