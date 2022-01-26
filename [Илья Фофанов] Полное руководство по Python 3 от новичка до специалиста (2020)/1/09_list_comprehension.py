greeting = 'Hello world'
chars = []

for l in greeting:
    chars.append(l)

print(chars)

chars = [l for l in greeting]
print(chars)

numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

numbers = [n for n in range(0, 11)]
print(numbers)

numbers = [n * n for n in range(0, 11)]
print(numbers)

numbers = [n * n for n in range(0, 11) if n % 2 != 0]
print(numbers)

len_in_centimeters = [12, 20, 25, 24, 64, 23]
len_in_inches = [(round(cm / 2.45, 2)) for cm in len_in_centimeters]
print(len_in_inches)

list_1 = [2, 4 - 6, 4 - 6, 8 - 4]
list_2 = [2, -6, 6, 4 - 7, -4, 7]
pairs = []

for x in list_1:
    for y in list_2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))

print(pairs)

pairs = [(x, y) if x + y == 0 else None for x in list_1 for y in list_2]
print(pairs)
