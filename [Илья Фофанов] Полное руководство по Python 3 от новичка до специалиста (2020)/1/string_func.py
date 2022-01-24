str = "Hello my name is Aleks"
length = len(str)
print(length)

print(str.count("l"))
print(str.capitalize())

print(str.upper())
upperd = str.upper()

print(str.lower())
lowered = str.lower()

print(lowered.islower())
print(upperd.isupper())

print("123abs".isalnum())
print("123abs!".isalnum())
print("123abs!".isalpha())
print("abs".isalpha())

print("  ".isspace())
print("".isspace())

empty_string = " "
print(empty_string.strip(' ') == "")

if not empty_string:
    print("not empty")
else:
    print("empty")

h = "hello"
print(h.startswith("he"))
print(h.endswith("lo"))

split = h.split("l")
print(type(split))
print(split)

data = "12;20;5;345;40"
print(data.split(";"))
