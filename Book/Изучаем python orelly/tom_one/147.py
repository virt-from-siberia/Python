D = {'food': 'spam', 'quantity': 1, 'color': 'pink'}
print(D)
print(D['food'])

D['quantity'] += 1
print(D)

newD = {}
newD['name'] = 'Bob'
newD['job'] = 'developer'
newD['age'] = 40
print(newD)

bob1 = dict(name=40, job='front', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['alex', 'python developer', 36]))
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Hakkinen'},
       'job': ['dev', 'mgr'], 'age': 40}

print(rec['name']['first'])
print(rec['job'])
rec['job'].append('junior')
print(rec)
