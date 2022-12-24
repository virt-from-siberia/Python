from fastapi import FastAPI
from . import schemas


app = FastAPI()


@app.post('/blog')
def create(requet: schemas.Blog):
    return requet
