my_set = set()
print(my_set)
print(type(my_set))

my_set.add(1)
print(my_set)

my_set.add(2)
print(my_set)

my_set.add(2)
print(my_set)

my_list = [
    1, 1, 1, 2, 3, 5, 5, 5, 7, 4, 34, 4, 7, 4, 6445, 56, 7, 7,
]

new_set = set(my_list)
print(new_set)
print(len(new_set))

print(1 in new_set)
print(5 in new_set)

set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5}

print(set_1.issubset(set_2))
print(set_2.issubset(set_1))

print(set_2.issubset(set_1))
print(set_1.issubset(set_2))

set_3 = {1, 2, 5}
set_4 = {17, 25, 54}

print(set_3.isdisjoint(set_4))
print(set_4.isdisjoint(set_3))

set_5 = {0, 1, 2, 3, 4}
set_6 = {1, 2, 3, 4, 5}
set_dif = set_5.difference(set_6)
set_sim = set_5.symmetric_difference(set_6)
print(set_dif)
print(set_sim)

set_5.update(set_6)
print(set_5)

set_5.remove(1)
print(set_5)

set_5.discard(41)
print(set_5)

popped_out_element = set_5.pop()
print(popped_out_element)

set_5.clear()
print(set_5)
