class Character():
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.damage = damage
        self._health = 100
        self.__race = race
        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


Character.MAX_SPEED = 10
c = Character('Ork')

print(c.current_speed)
c.current_speed = 99
print(c.current_speed)
c.current_speed = 205
print(c.current_speed)
