numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    print(number)

range_numbers = range(1, 6)
print(range_numbers)

for i in range_numbers:
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

new_numbers = [1, 3, 5, 9]
for i, item in enumerate(new_numbers):
    new_numbers[i] *= 2
print(new_numbers)

name = 'John'
for i in name:
    print(i)

for _ in range(5):
    print('Alarm')

person = ('John', 'Silver', 22)
for i in person:
    print(i)

persones = [
    ('John', 22),
    ('Bob', 24),
    ('Alex', 24),
]
print(len(persones))

for (name, age) in persones:
    print(f"name = {name}, age = {age} years old")

players = dict(Calsen=2754, Alex=3847, Shumaher=57456)
print(players)

for item in players.items():
    for k, v in players.items():
        print(f"{k} has raiting {v}")

for v in players.values():
    print(v)

# find all

list_1 = [2, 4, 5 - 6, -3, 6, -99, 4, 7, -6, 4, -6, -55, 456]
list_2 = [2, -6, 8, 4 - 2, -5, 66, -44, -8, 6]

pairs = []
for x in list_1:
    for y in list_2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))

print(pairs)
