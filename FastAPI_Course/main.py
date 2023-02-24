from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import ValidationError
from typing import List, Optional

from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI(
    title='Training app'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'programmer', 'name': 'Alexander'},
    {'id': 3, 'role': 'devops', 'name': 'Ivan'},
    {'id': 4, 'role': 'devops', 'name': 'Alex', "degree":
        [
            {"id": 1, "created_at": "2015-02-10", "type_degree":  "expert"}
        ]
     },
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC',
        'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC',
        'side': 'sell', 'price': 125, 'amount': 2.12},
]


@app.exception_handler(ValidationError)
async def validation_exeption_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({
                                                                                   "detail": exc.errors()})
    )


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: str
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.get('/users/{user_d}', response_model=List[User])
def get_users(user_id: int):
    return [user for user in fake_users if user.get('id', 0) == user_id]


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)

    return {
        "status": 200, "data": fake_trades
    }
