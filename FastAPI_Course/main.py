from fastapi import FastAPI

app = FastAPI(
    title='Training app'
)

fake_users = [
    {'id': 1, ' role': 'admin', 'name': 'Bob'}
    {'id': 2, ' role': 'programmer', 'name': 'Alexander'},
    {'id': 3, ' role': 'devops', 'name': 'Ivan'},
]


@app.get('/users/')
def get_users():
    pass
