L = [123, 'spam', 12.3]
len(L)
L[0]
L[:-1]
L + [1, 2, 3]

L.append('NI')
L.pop(2)

M = ['cc', 'aa', 'bb', 'ee', 'd', 'e', ]
M.sort()
print(M)

M.reverse()
print(M)

# L[99] = 12
# print(L)

NL = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
print(NL)
print(NL[1][2])

print('==========')
col12 = [row[0] for row in NL]
print(col12)

print('==========')
new_col = [row[0] + 1 for row in NL]
print(new_col)

print('==========')
new_col_filtered = [row[1] + 1 for row in NL if row[1] % 2 == 0]
print(new_col_filtered)

diag = [NL[i][i] for i in [0, 1, 2]]
print('diag', diag)

print(list(range(4)))
print(list(range(-2, 6, 1)))
print([[x ** 2, x ** 3] for x in range(4)])

print('==========')
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

print('==========')
