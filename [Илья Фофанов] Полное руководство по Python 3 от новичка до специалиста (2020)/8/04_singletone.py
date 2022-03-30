class Character:
    def __init__(self):
        self.race = 'Elf'


c = Character()
print(c.race)


class Character():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = 'Elf'


c = Character()
print(c.race)
