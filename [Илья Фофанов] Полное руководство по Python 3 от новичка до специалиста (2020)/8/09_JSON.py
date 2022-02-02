import json
import requests


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year


tournaments = {
    "Aeroflot Open": 2010,
    "FIDE World Cup": 2018,
    "FIDE Grand Prix": 2016,
}

json_data = json.dumps(tournaments, indent=2)
print(json_data)

loaded = json.loads(json_data)
print(type(loaded))
print(loaded)

t1 = Tournament('Aeroflot Open', 2010)

json_data = json.dumps(t1.__dict__)
print(json_data)

t = Tournament(**json.loads(json_data))
print(f"name={t.name}, year={t.year}")


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments


t1 = Tournament('Aeroflot Open', 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament('FIDE Grand Prix', 2016)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1.__dict__, default=lambda obj: obj.__dict__)
print(json_data)

decoded_player = ChessPlayer(**json.loads(json_data))
print(decoded_player)

player_tournaments = decoded_player.tournaments
print(type(player_tournaments))
print(player_tournaments[0])


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournamentsx = list(map(Tournament.from_json(), json_data["tournaments"]))
        return cls(tournamentsx)


t1 = Tournament('Aeroflot Open', 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament('FIDE Grand Prix', 2016)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)
print(type(json_data))
print(json_data)

print("======")
print(decoded_player)
print(decoded_player.tournaments)

with open('player.json', 'w') as file:
    json.dump(p1, file, default=lambda obj: obj.__dict__)

with open('player.json', 'r') as read_file:
    data = json.load(read_file)

print(data)

response = requests.get('https://jsonplaceholder.typicode.com/posts')
todos = json.loads(response.text)
print('=====todos====')
print(todos)

with open('posts.json', 'w') as file:
    json.dump(todos, file, default=lambda obj: obj.__dict__)

with open('posts.json', 'r') as read_file:
    data = json.load(read_file)

print(data)
