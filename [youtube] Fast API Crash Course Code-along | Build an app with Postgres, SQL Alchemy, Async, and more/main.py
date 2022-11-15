from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


users = []


class User(BaseModel):
    email: str
    id: int
    is_active: bool
    bio: Optional[str]


@app.post("/users")
async def crete_user(user: User):
    users.append(user)
    return {"user": user}


@app.get("/users", response_model=List[User])
async def get_user():
    return users


@app.get('/users/{id}')
async def get_user_by_id(
        id: int = Path(
            ..., description='The id of youser you want ot retrive', gt=1,),
        q: str = Query(None, max_length=5)
):
    return {
        "user":  users[id],
        "query": q
    }
