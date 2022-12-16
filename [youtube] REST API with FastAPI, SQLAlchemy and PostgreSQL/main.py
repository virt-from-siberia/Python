from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()


class Item(BaseModel):
    id: int
    name : str
    price: str
    description: str
    on_offer: bool

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()    
    return items


@app.get('/item/{item_id} ')
def get_item(item_id: int):
    pass


@app.post('/item', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item : Item):
    print("item", item)
    new_item = models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer,
    )
       
    
    db_item = db.query(models.Item).filter(item.name == new_item.name).first()
    print(db_item)
    
    if db_item is not None:
        raise HTTPException(status_code=400, detail="item already exists")
    
    db.add(new_item)
    db.commit() 
    
    return new_item


@app.get('/item/{item_id}')
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
