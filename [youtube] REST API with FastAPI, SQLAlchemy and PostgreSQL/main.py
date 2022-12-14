from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()


class Item(BaseModel):
    id: int
    namcription: str
    price: str
    description: int
    on_offer: bool

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    item = db.query(models.Item).all()


@app.get('/item/{item_id} ')
def get_item(item_id: int):
    pass


@app.post('/items')
def create_item():
    pass


@app.get('/item/{item_id} ')
def update_item(item_id: int):
    pass


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
    pass


# @app.get('/')
# def index():
#     return {"message": "hello wordl"}


# @app.get('/greet/{name}')
# def greet_name(name: str):
#     return {"greeting": f"hello {name}"}


# @app.get('/grret')
# def greet_optional_name(name: Optional[str] = "user"):
#     return {"mesage": f"hello {name}"}


# @app.put('/item/{iten_id}')
# def update_item(item_id: int, item: Item):
#     return {
#         "id": item_id,
#         "name": item.name,
#         "description": item.description,
#         "price": item.price,
#         "on_offer": item.on_offer
#     }
