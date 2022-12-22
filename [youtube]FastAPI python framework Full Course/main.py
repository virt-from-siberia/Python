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
def ablout():
    return {
        "data": {
            "name": "about",
        }
    }
