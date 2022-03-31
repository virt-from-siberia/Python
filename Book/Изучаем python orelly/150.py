D = {'a': 1, 'b': 2, 'c': 3}
print('f' in D)
print('a' in D)

if not 'f' in D:
    print('F is missing')


print('=====')
value = D.get('x', 0)
print(value)

print('=====')
value = D['x'] if 'x' in D else 1
print(value)
