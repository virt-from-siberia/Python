from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'I am - {} , name -{}, fullness - {}, '.format(
            self.name,
            self.name,
            self.fullness,
        )

    def bay_food(self):
        if self.house.money <= 10:
            self.work()
        else:
            cprint('{} bay food'.format(self.name), color='green')
            self.house.money -= 10
            self.house.food += 10

    def eat(self):
        if self.house.food <= 10:
            cprint('{} hav been eating'.format(self.name), color="yellow")
            self.fullness += 20
            self.house.food -= 10
        else:
            print('have not food')

    def work(self):
        cprint('{} went to work'.format(self.name), color="green")
        self.house.money += 50
        self.fullness -= 20

    def play(self):
        print('{} play dota'.format(self.name))
        self.fullness -= 10

    def go_to_house(self, house):
        self.house = house
        cprint('{} enter the home'.format(self.name), color="cyan")
        self.fullness -= 10

    def act(self):
        if self.fullness <= 10:
            self.eat()

        dice = randint(1, 6)
        if dice == 1:
            self.work()
        if dice == 2:
            self.eat()
        else:
            self.play()


class House:

    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'In my house eat : {}, money : {}'.format(self.food, self.money)


citizens = [
    Man(name='Bivis'),
    Man(name='Badhead')
]
# man = Man(name='Valusa')
# beavis = Man(name='Bivis')
# badhead = Man(name='Badhead')

house = House()

for day in range(1, 21):
    print('============= day : {} ============'.format(day))
    for citizen in citizens:
        citizen.go_to_house(house=house)
        citizen.act()
        print(citizen)
