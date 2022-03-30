class Vehicle:

    def __init__(self, position):
        self.position = position

    def calculate_route(self, source, to):
        return 0

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    def move_along(self, route):
        print("moving")


class Car(Vehicle):
    pass


class Airplane(Vehicle):
    pass


class RadioMixin:

    def __init__(self):
        self.radio = Radio()

    def turn_on(self, station):
        self.radio.set_station(station)
        self.radio.play()


class Radio:
    def set_station(self, station):
        self.station = station

    def play(self):
        print(f"playing {self.station}")


class Car(Vehicle, RadioMixin):
    def __init__(self):
        Vehicle.__init__(self, (10, 20))
        RadioMixin.__init__(self)


car = Car()
car.turn_on('Moscow FM')




