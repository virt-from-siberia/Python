a, b = 1, 2

for element in [(1, 2), (3, 4)]:
    a, b = element[0], element[1]
    print(a + b)

zoo_pets = [
    'lion', 'skuns', 'elephant', ' horse'
]

for animal in  zoo_pets:
    print(animal)
    del zoo_pets[0]
print(zoo_pets)

for a, b in [(1, 2), (3, 4)]:
    print(a + b)