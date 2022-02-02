numbers = [1, 2, 3]


class Character():
    max_speed = 100
    dead_health = 0

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.heath = 100

    def hit(self, damage):
        self.heath -= damage

    def is_dead(self):
        return self.heath == self.dead_health


unit = Character('Elf', damage=30, armor=50)

print(unit.race)
print(unit.damage)
print(unit.armor)
print(Character.max_speed)

unit.hit(20)
print(unit.heath)
print(unit.is_dead())

unit.hit(80)
print(unit.heath)
print(unit.is_dead())
