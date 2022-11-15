from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import user, sections, courses

app = FastAPI(
    title='My app',
    description="",
)

app.include_router(user.router)
app.include_router(sections.router)
app.include_router(courses.router)
