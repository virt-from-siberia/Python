class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


my_backpack = Backpack()
my_backpack.add(item='ноутбук')
print(bool(my_backpack), len(my_backpack))
if my_backpack:
    print('Рюкзак не пуст!')
    print('В нем лежит', len(my_backpack), 'предметов')
else:
    print('Вот рюкзак пустой, он предмет простой...')

