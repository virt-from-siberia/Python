from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session


from . import models
from .database import engine, get_db

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


my_posts = [
    {
        "id": 1,
        "title": "Post 1",
        "content": "This is post 1",
        "published": True,
        "rating": 1
    },
    {
        "id": 2,
        "title": "Post 2",
        "content": "This is post 2",
        "published": False,
        "rating": 2
    },
]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
async def root():

    return {"message": "Hello World"}


@app.get('/sqlalchemy')
def test_posts(db: Session = Depends(get_db)):
    return {
        "status": "success",
    }


@app.get('/posts')
async def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()

    return {"data": posts}


@app.post('/posts')
async def create_posts(post: Post):
    cursor.execute(
        """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
        (post.title, post.content, post.published))

    new_post = cursor.fetchone()
    conn.commit()

    return {"post": new_post}


@app.get('/posts/{id}', status_code=status.HTTP_201_CREATED)
def get_post(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    return {"post_detail": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id,))
    deleted_post = cursor.fetchone()
    conn.commit()

    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
        (post.title, post.content, post.published, id))

    updated_posts = cursor.fetchone()
    conn.commit()

    if not updated_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")

    return {"post": updated_posts}
