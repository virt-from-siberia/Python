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
    # rating: Optional[int] = None


def _file_post(id: int):
    for post in my_posts:
        if post['id'] == id:
            return post


def _find_index_post(id: int):
    for i, p in enumerate(my_posts):
        print('i', i)
        print('p', p)
        if p['id'] == id:
            return i


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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    return {"post_detail": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    post = _file_post(id)
    index = _find_index_post(id)
    if not index or not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = _find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"post": post_dict}
