from collections import namedtuple

players = [
    ('Carlson', 1990, 2008),
    ('Mikelele', 1990, 2308),
    ('Shumaher', 1990, 2458)
]

print(players[0])

Player = namedtuple('Player', 'name age rating')

players_new = [
    Player('Carlson', 1990, 2008),
    Player('Mikelele', 1998, 2308),
    Player('Shumaher', 1985, 2458),
]

print(type(Player))
print(players_new[0])
print(type(players_new[0]))
print(players_new[0].name)

p1 = Player('Alex', 1985, 29394)
