from fastapi import FastAPI

app = FastAPI(
    title='Training app'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'programmer', 'name': 'Alexander'},
    {'id': 3, 'role': 'devops', 'name': 'Ivan'},
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC',
        'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC',
        'side': 'sell', 'price': 125, 'amount': 2.12},
]

fake_users2 = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'programmer', 'name': 'Alexander'},
    {'id': 3, 'role': 'devops', 'name': 'Ivan'},
]


@app.get('/users/')
def get_users(user_id: int):
    return [user for user in fake_users if user.get('id', 0) == user_id]


@app.get('/trades/')
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]


@app.post('/users/')
def update_user(user_id: int, new_name: str, new_role: str):
    current_user = list(
        filter(lambda user: user.get('id') == user_id, fake_users2))[0]

    if new_name:
        current_user['name'] = new_name
    if new_role:
        current_user['role'] = new_role

    return {"status": 200, "data": current_user}

