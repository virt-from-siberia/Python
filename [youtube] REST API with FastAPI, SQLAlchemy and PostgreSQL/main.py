from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    id: int
    namcription: str
    prie: str
    desce: int
    on_offer: bool


@app.get('/')
def index():
    return {"message": "hello wordl"}


@app.get('/greet/{name}')
def greet_name(name: str):
    return {"greeting": f"hello {name}"}


@app.get('/grret')
def greet_optional_name(name: Optional[str] = "user"):
    return {"mesage": f"hello {name}"}


@app.put('/item/{iten_id}')
def update_item(item_id: int, item: Item):
    return {
        "id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "on_offer": item.on_offer
    }
