from typing import Optional, List
from fastapi import FastAPI, Path, Query
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


users = [] 


class User(BaseModel):
    email: str
    id: int
    is_active: bool
    bio: Optional[str]


@router.post("/users/{id}")
async def crete_user(id: int, user: User):
    users.append(user)
    return {"user": user}


@router.get("/users", response_model=List[User])
async def get_user():
    return users


@router.get('/users/{id}')
async def get_user_by_id(
        id: int = Path(
            ..., description='The id of youser you want ot retrive', gt=1,),
        q: str = Query(None, max_length=5)
):
    return {
        "user":  users[id],
        "query": q
    }
