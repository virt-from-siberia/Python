
i = 1
while i < 10:
    i = i * 2
    print(i)


f1, f2 = 1, 1
while f2 < 1000:
    print(f2)
    next_f2 = f1 + f2
    next_f1 = f2
    f1, f2 = next_f1, next_f2

my_pets = ['cat', 'dog', 'hamster']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print(pet)
    if pet == 'cat':
        print('hello cat!')
    i += 1
print('cood bay')
