import itertools as it

iterable = [1, 2, 3]

iterator = iter(iterable)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

even_numbers = it.count(0, 2)
print(even_numbers)

print(list(next(even_numbers) for _ in range(5)))
print(list(zip(it.count(), ['a', 'b', 'c'])))


def print_iterable(iterable, end=None):
    for x in iterable:
        if end:
            print(x, end=end)
        else:
            print(x)


ones = it.repeat(1, 5)
print(print_iterable(ones, ' '))

print(list(map(pow, range(10), it.repeat(2))))

pos_neg_ones = it.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(10)))

letters = it.cycle(['A', 'B', 'C'])
print(list(next(letters) for _ in range(10)))

print(list(it.accumulate([1, 2, 3, 4, 5])))
print(list(it.accumulate(['A', 'B', 'C', 'D'])))
print(list(it.chain('ABC', 'DEF')))
print(list(it.chain.from_iterable(['ABC', 'DEF'])))
print(list(it.chain([1, 2, 3], [4, 5, 6])))

print(list(it.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5, 6])))

iterable = iter([1, 2, 3])
print(iterable)
