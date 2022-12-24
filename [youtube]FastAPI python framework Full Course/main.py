from typing import Optional
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.get('/')
def index():
    return {
        "data": {
            "name": "Aleksey",
        }
    }


@app.get('/about')
def about():
    return {
        "data": {
            "name": "about",
        }
    }


@app.get('/blog')
def index(limit=10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {
            "data": {
                "name": f"{limit} published blogs from the db",
            }
        }
    else:
        return {
            "data": {
                "name": f"{limit} all blogs from the db",
            }
        }


@app.get('/blog/unpublished')
def show_unpublished(id: int):
    return {
        "data": "all unpublished blogs "
    }


@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": id
    }


@app.get('/blog/{id}/comments')
def show_comments(id: int, limit=10):

    return {
        "data": {'1', '2 '}
    }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):

    return {
        "data":  f"Blog was created with title as {request.title}"
    }


# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=9000)
