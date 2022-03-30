players = {
    'Carlsen': 2345,
    'Caruana': 1800,
    'Alejev': 1600,
    'Shumaher': 2800
}

players = dict(Carlsen=2345, Caruana=1800, Alejev=1700, Shumaher=2890)

print(players['Carlsen'])

players['So'] = 760
print(players)

players['So'] = 765
print(players)

del players['So']
print(players)

keys = players.keys()
print(type(keys))

li = list(keys)
print(li)

print('Shumaher' in players)
print('So' in players)
print('So' not in players)

vals = players.values()
print(type(vals))
print(vals)

list_vals = list(players.values())
print(list_vals)

players_copy = players.copy()
print(players_copy)

for k, v in players_copy.items():
    print(type(k))
    print(type(v))
    print(k, v)

items = players_copy.items()
print(type(items))

players.pop('Caruana')
print(players)
print(players.popitem())
print(players_copy.popitem())

players.setdefault('Lol')
print(players)


