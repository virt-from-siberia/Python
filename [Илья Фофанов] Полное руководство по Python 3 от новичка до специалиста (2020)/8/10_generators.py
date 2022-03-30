import random
import itertools


def randoms(min, max, n):
    return [random.randint(min, max) for _ in range(n)]


for r in randoms(10, 30, 5):
    print(r)


def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


for r in randoms(10, 30, 5):
    print(r)

rand_sequence = randoms(1, 10, 10)
print(rand_sequence)

seq = list(randoms(10, 10, 50))
print(seq)


def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


rand_sequence = randoms(1, 10, 10)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


def randoms(min, max):
    while True:
        yield random.randint(min, max)


rand_sequence = randoms(1, 10000)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


def read_line_by_line(file):
    while True:
        line = file.readline()
        if not line:
            break
        yield line


rand_sequence = randoms(1, 10)
n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)

my_list = [1, 2, 3, 4]

squares = [x ** 2 for x in my_list]
print(squares)

squares = (x ** 2 for x in my_list)

for i in squares:
    print(i)
