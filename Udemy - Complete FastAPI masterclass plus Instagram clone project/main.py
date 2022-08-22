from fastapi import FastAPI
from router import blog_get, blog_post
from router import user
from db import models
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/hello')
def index():
    return {'message': 'hello world'}


models.Base.metadata.create_all(engine)
