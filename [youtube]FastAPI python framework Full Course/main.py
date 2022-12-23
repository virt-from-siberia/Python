from fastapi import FastAPI, APIRouter


app = FastAPI()


@app.get('/')
def index():
    return {
        "data": {
            "name": "Aleksey",
        }
    }


@app.get('/about')
def about():
    return {
        "data": {
            "name": "about",
        }
    }


@app.get('/blog/unpublished')
def show_unpublished(id: int):
    return {
        "data": "all unpublished blogs "
    }


@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": id
    }


@app.get('/blog/{id}/comments')
def show_comments(id: int):
    return {
        "data": {'1', '2 '}
    }
