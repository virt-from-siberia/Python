int_list = [1, 2, 3]
mixed_list = [1, 2.0, "lol"]

print(len(int_list))
print(len(int_list))
print(int_list[0])
print(int_list[-1])
print(int_list[1:])

lint_names = ["John", "Bob", "Elis"]
lint_names2 = ["Alex", "Ivan", "Jim"]

names_combined = lint_names + lint_names2
print(names_combined)

names_combined[1] = "Elena"
print(names_combined)

names_combined.append("William")
names_combined.append("James")
print(names_combined)

names_popped = names_combined.pop()
print(names_popped)
print(names_combined)

names_combined.pop(0)
print(names_combined)

names_combined.append("John")
name_sorted = names_combined.sort()
print(name_sorted)

letters = ['ac', 'ab', 'aa']
letters.sort()
print(letters)

letters = ['abc', 'a', 'ab']
letters.sort(key=len)

numbers = [3, 2, 6, 18, 5, 79797, 5]
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers.insert(1, 22)
print(numbers)

print(numbers.index(5))
print(numbers.count(5))

copy = numbers.copy()
print(copy)
