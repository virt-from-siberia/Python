lst = [1, 2, 3, 4, 5]

print(repr(lst))
print(repr(lst) == lst)
print(eval(repr(lst)) == lst)


class Character():

    def __init__(self, race, damage=100):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __str__(self):
        return f"{self.race} with damage {self.damage}"

    def __eq__(self, other):
        if instance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False


c = Character('Eth', 100)
print(c)

d = eval(repr(c))
print(d)
print(d == c)
