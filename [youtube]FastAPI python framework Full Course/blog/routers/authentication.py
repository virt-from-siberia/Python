from fastapi import APIRouter


router = APIRouter()


router = APIRouter(
    tags=['auth'],
)


@router.post('/login')
def login():
    return "login"
