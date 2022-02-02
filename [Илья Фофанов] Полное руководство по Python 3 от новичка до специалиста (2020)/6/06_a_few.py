class Animal:
    def die(self):
        print('bye-bye')
        self.heaith = 0


class Carnivour:
    def hunt(self):
        print('eating')
        self.satiety = 100


class Dog(Animal, Carnivour):
    def bark(self):
        print('woof-woof')


dog = Dog()
dog.bark()
dog.hunt()
dog.die()


class Animal:
    def set_health(self, health):
        print('set in animal')


class Carnivour(Animal):
    def set_health(self, health):
        print('set in Carnivour')


class Mammal(Animal):
    def set_health(self, health):
        print('set in Mammal')


class Dog(Mammal, Carnivour):
    pass
