from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import sections, courses, users
from db.db_setup import SessionLocal, engine
from db.models import course, user


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='My app',
    description="",
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
