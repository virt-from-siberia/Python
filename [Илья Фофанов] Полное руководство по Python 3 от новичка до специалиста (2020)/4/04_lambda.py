def square(*args):
    return [x * x for x in args]


result = square(1, 2, 3, 4, 5)
print(result)


def triple(*args):
    return [x * 3 for x in args]


result = triple(1, 2, 3, 4, 5)
print(result)


def square(number: int) -> int:
    return number * number


numbers = [1, 2, 3, 4, 5]

mapped = map(square, numbers)
print(mapped)
print(type(mapped))

for x in mapped:
    print(x)

print(list(map(square, numbers)))


def is_adult(age: int) -> bool:
    return age >= 18


ages = [14, 16, 18, 21, 12]
filtered = filter(is_adult, ages)
print(filtered)

for x in filtered:
    print(x)

multiplayer = lambda x, y: x * y
res = multiplayer(2, 3)
print(res)
