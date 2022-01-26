from collections import OrderedDict

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'a'
d2['c'] = 'C'

d3 = {}
d3['a'] = 'A'
d3['b'] = 'b'
d3['c'] = 'C'

print(d1)
print(d1 == d2)
print(d1 == d3)

for k, v in d1.items():
    print(k, v)

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'a'
d2['c'] = 'C'

d3 = OrderedDict()
d3['a'] = 'A'
d3['b'] = 'b'
d3['c'] = 'C'

print(d1)
print(d1 == d2)
print(d1 == d3)


