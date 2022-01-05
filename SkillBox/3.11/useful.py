zoo_pets = [
    'lion', 'skuns', 'elepant', 'horse'
]

for i, animal in enumerate(zoo_pets):
    print(i, animal)

for i in range(100, 600, 50):
    print(i)

for animal in zoo_pets:
    for char in animal:
        print(char)
    print(animal)

for animal in zoo_pets[::2]:
    print(animal)

an = 'dog'
for char in an:
    print(char)

zoo_pets_mass = {
    'lion': 300,
    'skuns': 5,
    'elepant': 5000,
    'horse': 400
}

total_mass = 0
for mass in zoo_pets_mass.values():
    print(mass)
    total_mass += mass
print('Общяя масса животных', total_mass)
