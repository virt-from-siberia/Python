import pickle


class Character():

    def __init__(self, race, damage=10):
        self.race = race
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health = 100

    def is_dead(self):
        return self.health == 0


c = Character('Elf')
c.hit(10)
print(c.is_dead())

with open(r'C:\\game_state.txt', 'w+b') as f:
    pickle.dump(c, f)
