from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()


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
    rating: Optional[int] = None


def _file_post(id: int):
    for post in my_posts:
        if post['id'] == id:
            return post


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/posts')
async def get_posts():
    return {"data": my_posts}


@app.post('/posts')
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000000)
    my_posts.append(post_dict)

    return {"post": post_dict}


@app.get('/posts/{id}', status_code=status.HTTP_201_CREATED)
def get_post(id: int, response: Response):

    post = _file_post(id)
    if not post:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")

    return {"post_detail": post}
