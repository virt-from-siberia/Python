S = 'spammy'
S = S.replace('mm', 'xx')
print(S)

print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(where)

S = S[:where] + 'EGGS' + S[:where + 4]
print(S)
S.replace('SPAM', 'EGGS')
print(S)


S = 'spammy'
L = list(S)
print(L)


L[3] ='x'
L[4] ='x'

print(L)

S = ''.join(L)
print(S)