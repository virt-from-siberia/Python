print(abs(-1))

print(max(1, 3, 5, 7, 65, 4, 5, 67))
print(min([1, 3, 5, 7, 65, 4, 5, 67]))

print(pow(2, 9))

print(round(2.37, 1))

print(sum([1, 54, 3, 5, 6, 67, 567, 567, 567]))

h = hex(42)
o = oct(42)
b = bin(42)
print(h)
print(o)
print(b)

all_true_1 = all([True, True, True])
all_true_2 = all([True, False, True])
print(all_true_1)
print(all_true_2)

players = [
    ('Carlsen', 1834),
    ('Alonso', 3453),
    ('Shumaher', 45645),
    ('Giri', 4545),
]

print(all([rating > 2700 for _, rating in players]))
print(any([rating > 2700 for _, rating in players]))

letters = 'abcd'
numbers_new = (10, 20, 30)
zipped = zip(letters, numbers_new)

print(type(zipped))

zipped_list = list(zipped)
print(zipped_list)

names = ['Alonso', 'Truli', 'Button', 'Coulthard']
ratings = [2343, 23234, 2323, 43254]

players = dict(zip(names, ratings))
print(players)

reply = input()
print(reply)

code = ord('a')
