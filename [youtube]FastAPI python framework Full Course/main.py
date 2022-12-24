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


@app.get('/blog')
def index(limit, published=False):
    if published:
        return {
            "data": {
                "name": f"{limit} published blogs from the db",
            }
        }
    else:
        return {
            "data": {
                "name": f"{limit} all blogs from the db",
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
