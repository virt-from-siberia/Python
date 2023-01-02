
from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    firstname: str
    lastname: str
    email: str
    blogs: List

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
