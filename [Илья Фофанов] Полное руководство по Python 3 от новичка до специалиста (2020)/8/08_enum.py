from enum import Enum, IntEnum


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


red = TrafficLight.RED
print(red)
print(TrafficLight.RED.name)
print(TrafficLight.RED.value)

for c in TrafficLight:
    print(c.name)


class Priority(IntEnum):
    LOW = 1
    NORMAL = 2
    HIGH = 3


print(Priority.LOW < Priority.NORMAL)


class Color(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 4


combination = Color.RED | Color.GREEN
print(combination)


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    EARTH = (5.976e+24, 6.37814e6)
    JUPITER = (1.9e+27, 7.1492e7)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self):
        G = 6.67300e-11
        return G * self.mass / (self.radius * self.radius)


print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)
